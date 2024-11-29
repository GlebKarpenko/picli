from PIL import Image
from picli import resource_manager as mn

def parse_metric(metric_pair):
    """
    Parses a coordinate value which can be an integer or a percentage string.
    Returns the value as a tuple of (type, value), where type is 'px' or '%'.
    """
    if metric_pair.endswith('%'):
        try: 
            return ('%', float(metric_pair[:-1]))
        except ValueError:
            raise ValueError(mn.get_tools_error("metric_wrong_percent", metric_pair))
    else:
        try:
            return (('px'), int(metric_pair))
        except ValueError:
            raise ValueError(mn.get_tools_error("metric_wrong_pixel", metric_pair))

def scale_metric(metric_pair, image_scale):
    """
    Converts percentage values to image scale
    """
    dtype, value = metric_pair

    if (dtype == '%'
        and value > 0 
        and value < 100):
        scaled_value = int(value / 100 * image_scale)
        return scaled_value
    elif isinstance(value, int): 
        return value
    else: 
        return 0
    
def get_supported_file_extensions():
    exts = Image.registered_extensions()
    return {ex for ex, f in exts.items() if f in Image.OPEN}

def get_file_extension(filename):
    return '.' + filename.lower().split('.')[-1]