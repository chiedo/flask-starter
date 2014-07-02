var gulp = require('gulp');
var shell = require('gulp-shell');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var del = require('del');
var sass = require('gulp-sass');
minifyCSS = require('gulp-minify-css');

var paths = {
  scripts: ['webapp/static/js/dev/global.js','webapp/static/js/dev/**/*.js'],
  css: ['webapp/static/css/dev/global.scss','webapp/static/css/dev/**/*.scss'],
  images: 'webapp/static/img/**/*'
};

gulp.task('sass', function () {
  gulp.src(paths.css)
    .pipe(sass())
    .pipe(minifyCSS({keepBreaks:false}))
    .pipe(concat('all.min.css'))
    .pipe(gulp.dest('webapp/static/css/build'));
});

gulp.task('clean', function(cb) {
  del(['build'], cb);
});

gulp.task('scripts', ['clean'], function() {
  // Minify and copy all JavaScript (except vendor scripts)
  return gulp.src(paths.scripts)
    .pipe(uglify())
    .pipe(concat('all.min.js'))
    .pipe(gulp.dest('webapp/static/js/build'));
});

gulp.task('images', ['clean'], function() {
 return gulp.src(paths.images)
    .pipe(imagemin({optimizationLevel: 5}))
    .pipe(gulp.dest('webapp/static/img'));
});

gulp.task('watch', function() {
  gulp.watch(paths.css, ['sass']);
  gulp.watch(paths.scripts, ['scripts']);
});

gulp.task('tests', function() {
  gulp.watch(['*.py','**/*.py'], shell.task([
    'nosetests --rednose --force-color --nocapture'
    //'nosetests --rednose --force-color --nocapture --with-coverage --cover-package=app.tests --cover-tests'
  ], { ignoreErrors: true }));
});

gulp.task('clear-pyc', function() {
  gulp.watch(['*.py','**/*.py'], shell.task([
    'find . -name "*.pyc" -exec rm "{}" ";"'
  ], { ignoreErrors: true }));
});

gulp.task('default', ['watch', 'scripts', 'images','tests','sass']);

