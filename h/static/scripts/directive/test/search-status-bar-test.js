'use strict';

var util = require('./util');

describe('searchStatusBar', function () {
  before(function () {
    angular.module('app', [])
      .directive('searchStatusBar', require('../search-status-bar'));
  });

  beforeEach(function () {
    angular.mock.module('app');
    angular.mock.module('h.templates');
  });

  it('should display the filter count', function () {
    var elem = util.createDirective(document, 'searchStatusBar', {
      filterActive: true,
      filterMatchCount: 5
    });
    assert.include($(elem).text(), "Found 5 results");
  });

  it('should display the selection count', function () {
    var elem = util.createDirective(document, 'searchStatusBar', {
      selectionCount: 1
    });
    assert.include($(elem).text(), 'Showing 1 selected annotation');
  });
});
