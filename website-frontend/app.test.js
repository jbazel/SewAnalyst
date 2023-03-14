'use strict';

const request = require('supertest');
const app = require('./server/app');

describe('Test all requests', () => {
    // LIST OF MOVIES

    test('GET /reportDownload/:reportName succeeds', () => {
        return request(app)
	    .get('/reportDownload/:reportName')
        .params({ reportName: 'report1.pdf' })
	    .expect(200);
    });

/*    test('GET /listOfMovies returns JSON', () => {
        return request(app)
	    .get('/listOfMovies')
	    .expect('Content-type', /json/);
    });

    test('GET /listOfMovies includes array', () => {
        return request(app)
	    .get('/listOfMovies')
        .expect(/\[.+\]/);
    });

    // filter by MOVIE

    test('GET /filterByMovie succeeds', () => {
        return request(app)
	    .get('/filterByMovie')
        .query({ movie: 'Inception' })
        .expect(200);
    });

    test('GET /filterByMovie returns JSON', () => {
        return request(app)
	    .get('/filterByMovie')
        .query({ movie: 'Inception' })
        .expect('Content-type', /json/);
    });

    test('GET /filterByMovie includes title, year, cast, reviews, rating', () => {
        return request(app)
	    .get('/filterByMovie')
        .query({ movie: 'Inception' })
        .expect(/Title/).expect(/Year/).expect(/Cast/).expect(/Reviews/).expect(/Rating/);
    });

    test('GET /filterByMovie includes an array', () => {
        return request(app)
	    .get('/filterByMovie')
        .query({ movie: 'Inception' })
        .expect(/\[.+\]/);
    });

    // Filter by RATING

    test('GET /filterByRating succeeds', () => {
        return request(app)
	    .get('/filterByRating')
        .query({ starRating: '10' })
        .expect(200);
    });

    test('GET /filterByRating returns JSON', () => {
        return request(app)
	    .get('/filterByRating')
        .query({ starRating: '10' })
        .expect('Content-type', /json/);
    });

    test('GET /filterByRating includes title, year, cast, reviews, rating', () => {
        return request(app)
	    .get('/filterByRating')
        .query({ starRating: '10' })
        .expect(/Title/).expect(/Year/).expect(/Cast/).expect(/Reviews/).expect(/Rating/);
    });

    test('GET /filterByRating includes an array', () => {
        return request(app)
	    .get('/filterByRating')
        .query({ starRating: '10' })
        .expect(/\[.+\]/);
    });

    test('GET /filterByRating includes review, date, title', () => {
        return request(app)
	    .get('/filterByRating')
        .query({ starRating: '10' })
        .expect(/review/).expect(/date/);
    });

    // LIST OF REVIEWS

    test('GET /listOfReviews succeeds', () => {
        return request(app)
	    .get('/listOfReviews')
	    .expect(200);
    });

    test('GET /listOfReviews returns JSON', () => {
        return request(app)
	    .get('/listOfReviews')
	    .expect('Content-type', /json/);
    });

    test('GET /listOfReviews includes array', () => {
        return request(app)
	    .get('/listOfReviews')
        .expect(/\[.+\]/);
    });
    // UPDATE MOVIE LIST

    test('GET /updateMovieList succeeds', () => {
        return request(app)
	    .get('/listOfReviews')
	    .expect(200);
    });

    test('GET /updateMovieList returns JSON', () => {
        return request(app)
	    .get('/listOfReviews')
	    .expect('Content-type', /json/);
    });

    test('GET /updateMovieList includes array', () => {
        return request(app)
	    .get('/listOfReviews')
        .expect(/\[.+\]/);
    });

    // POST adding a REVIEW

    test('POST /review succeeds', () => {
        const params = { ratingMovie: '5', review: 'average to be honest' };
        return request(app)
        .post('/review')
        .query({ nameOfMovie: 'Inception' })
        .send(params)
	    .expect(200);
    });

    // POST adding a MOVIE

    test('POST /movie/add succeeds', () => {
        const params = { movieTitle: 'Parasite', yearMovie: '2019', cast1: 'Yeo-jeong Cho', cast2: 'Park Seo-joon', cast3: 'Choi Woo-shik' };
        return request(app)
        .post('/movie/add')
        .send(params)
	    .expect(200);
    });*/
});
