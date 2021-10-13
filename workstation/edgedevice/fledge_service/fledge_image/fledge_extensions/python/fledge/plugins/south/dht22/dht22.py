# -*- coding: utf-8 -*-

# FLEDGE_BEGIN
# See: http://fledge.readthedocs.io/
# FLEDGE_END

""" Plugin for a DHT22 temperature and humidity sensor attached directly to the GPIO pins of a Raspberry Pi. """

from datetime import datetime, timezone
import copy
import logging

import adafruit_dht
from board import *

from fledge.common import logger
from fledge.plugins.common import utils
from fledge.services.south import exceptions

__author__ = "Oleksandr Ivanov"
__copyright__ = "Copyright (c) 2021 SoftServe"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"

index2pin = [
    D0, D1, D2, D3, D4, D5, D6, D7, D8, D9, 
    D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, 
    D20, D21, D22, D23, D24, D25, D26, D27 
]

_DEFAULT_CONFIG = {
    'plugin': {
        'description': 'DHT22 South Plugin',
        'type': 'string',
        'default': 'dht22',
        'readonly': 'true'
    },
    'assetName': {
        'description': 'Asset name',
        'type': 'string',
        'default': "dht22",
        'order': "1",
        'displayName': 'Asset Name',
        'mandatory': 'true'
    },
    'gpioPin': {
        'description': 'The GPIO pin into which the DHT11 data pin is connected', 
        'type': 'integer',
        'default': '4',
        'order': '3',
        'displayName': 'GPIO Pin'
    }    
}

_LOGGER = logger.setup(__name__)
""" Setup the access to the logging system of Fledge """
_LOGGER.setLevel(logging.INFO)


def plugin_info():
    """ Returns information about the plugin.

    Args:
    Returns:
        dict: plugin information
    Raises:
    """

    return {
        'name': 'DHT22 GPIO',
        'version': '1.9.0',
        'mode': 'poll',
        'type': 'south',
        'interface': '1.0',
        'config': _DEFAULT_CONFIG
    }


def plugin_init(config):
    """ Initialise the plugin.

    Args:
        config: JSON configuration document for the plugin configuration category
    Returns:
        handle: JSON object to be used in future calls to the plugin
    Raises:
    """

    handle = copy.deepcopy(config)
    return handle


def plugin_poll(handle):
    """ Extracts data from the sensor and returns it in a JSON document as a Python dict.

    Available for poll mode only.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
        returns a sensor reading in a JSON document, as a Python dict, if it is available
        None - If no reading is available
    Raises:
        DataRetrievalError
    """
    limit = 3
    for attempt in range(limit):
        try:
            indexpin = int(handle['gpioPin']['value']);
            pin = index2pin[indexpin];
            dht22 = adafruit_dht.DHT22(pin, use_pulseio=False)

            temperature = dht22.temperature
            humidity = dht22.humidity

            if humidity is not None and temperature is not None:
                time_stamp = utils.local_timestamp()
                readings = {'temperature': temperature, 'humidity': humidity}
                wrapper = {
                    'asset':     handle['assetName']['value'],
                    'timestamp': time_stamp,
                    'readings':  readings
                }
            else:
                raise exceptions.DataRetrievalError
        except Exception:
            # retry, DHT22 => Checksum did not validate. Try again.
            _LOGGER.info("DHT22 retry {} due to read error".format(attempt))
        else:
            return wrapper
    else:
        _LOGGER.info("DHT22 retried {} times, but values was not retrieved".format(limit))

def plugin_reconfigure(handle, new_config):
    """ Reconfigures the plugin, it should be called when the configuration of the plugin is changed during the
        operation of the south service.
        The new configuration category should be passed.

    Args:
        handle: handle returned by the plugin initialisation call
        new_config: JSON object representing the new configuration category for the category
    Returns:
        new_handle: new handle to be used in the future calls
    Raises:
    """
    _LOGGER.info("Old config for DHT22 plugin {} \n new config {}".format(handle, new_config))

    new_handle = copy.deepcopy(new_config)
    return new_handle


def plugin_shutdown(handle):
    """ Shutdowns the plugin doing required cleanup, to be called prior to the service being shut down.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
    Raises:
    """
    _LOGGER.info("DHT22 Poll plugin shutdown")