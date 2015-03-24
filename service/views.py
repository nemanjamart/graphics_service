from flask import current_app, Blueprint, request
from flask.ext.restful import Resource
from flask.ext.discoverer import advertise
import time
import inspect
import sys

from utils.graphics import get_graphics

blueprint = Blueprint(
      'graphics',
      __name__,
      static_folder=None,
)

class Graphics(Resource):
    """Return graphics information for a given bibcode"""
    scopes = []
    rate_limit = [1000,60*60*24]
    decorators = [advertise('scopes','rate_limit')]
    def get(self, bibcode):
       try:
           results = get_graphics(bibcode)
       except Exception, err:
           return {'msg': 'Unable to get results! (%s)' % err}, 500
       if results and results['query'] == 'OK':
           return results
       else:
           return {'msg': 'Unable to get results! (%s)' % results.get('error','NA')}, 404