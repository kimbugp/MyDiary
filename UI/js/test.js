'use strict';
var expect = require('chai').expect;
// mocha --require mock-local-storage

describe('test file', function() {
	it('should exist', function() {
		var profile = require('./profile.js');
		expect(profile).to.not.be.undefined;
	});
});