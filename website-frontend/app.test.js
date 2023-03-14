'use strict';

const request = require('supertest');
const app = require('./server/app');

describe('Test all requests', () => {

    // REPORT DOWNLOADS

    test('GET /reportDownload/:reportName succeeds', () => {
        return request(app)
	    .get('/reportDownload/report1.pdf')
	    .expect(200);
    });

    test('GET /reportDownload/:reportName returns file', () => {
        return request(app)
	    .get('/reportDownload/report1.pdf')
	    .expect('content-type', 'application/pdf');
    });

    //PROGRAM DOWNLOADS

    test('GET /program_download-win succeeds', () => {
        return request(app)
	    .get('/program_download-win')
	    .expect(200);
    });

    test('GET /program_download-win downloads a zip', () => {
        return request(app)
	    .get('/program_download-win')
	    .expect('content-type', 'application/zip');
    });

    test('GET /program_download-mac succeeds', () => {
        return request(app)
	    .get('/program_download-mac')
	    .expect(200);
    });

    test('GET /program_download-mac downloads a zip', () => {
        return request(app)
	    .get('/program_download-mac')
	    .expect('content-type', 'application/zip');
    });

    // LIST OF REPORTS

    
    test('GET /reportList succeeds', () => {
        return request(app)
	    .get('/reportList')
	    .expect(200);
    });

    test('GET /reportList contains JSON', () => {
        return request(app)
	    .get('/reportList')
	    .expect('Content-type', /json/);
    });

    test('GET /reportList includes array', () => {
        return request(app)
	    .get('/reportList')
	    .expect(/\[.+\]/);
    });

    // LIST OF REASONS

    test('GET /reportReasons/:reportName succeeds', () => {
        return request(app)
	    .get('/reportReasons/report1.pdf')
	    .expect(200);
    });

    test('GET /reportReasons/:reportName contains JSON', () => {
        return request(app)
	    .get('/reportReasons/report1.pdf')
	    .expect('Content-type', /json/);
    });

    test('GET /reportReasons/:reportName includes array', () => {
        return request(app)
	    .get('/reportReasons/report1.pdf')
	    .expect(/\[.+\]/);
    });

    // POST flagging a report

    test('POST /flagReport/:reportName succeeds', () => {
        const params = {reason: 'badness' };
        return request(app)
        .post('/flagReport/report1.pdf')
        .send(params)
	    .expect(302);
    });

});
