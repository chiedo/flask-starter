// This could be combined with the parent folders gulpfile if it is present.
// Separate now for clarity purposes

var gulp = require('gulp');
var browserify = require('gulp-browserify');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');

gulp.task('browserify', function() {
  gulp.src('main.js')
  .pipe(browserify({transform: 'reactify'}))
  .pipe(concat('react-bundle.js'))
  //.pipe(uglify())
  .pipe(gulp.dest('../static/js/build'));
});

gulp.task('default',['browserify']);

gulp.task('watch', function() {
  gulp.watch(["main.js", '**/*.*'], ['default']);
});
