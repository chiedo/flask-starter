var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('default', function() {
});

// Grunt is seeming better for tests. But will implement something
// else with gulp
gulp.task('tests', function() {
  gulp.watch('*.py', shell.task([
    'nosetests --rednose'
  ], { ignoreErrors: true }));
});

//Runs tests by default
gulp.task('default', ['tests']);
