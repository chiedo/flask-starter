var gulp = require('gulp');
var shell = require('gulp-shell');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var del = require('del');
var sass = require('gulp-sass');
var minifyCSS = require('gulp-minify-css');
var browserify = require('gulp-browserify');
var concat = require('gulp-concat');

var paths = {
  scripts: ['project/static/js/dev/global.js','project/static/js/dev/**/*.js'],
  css: ['project/static/css/dev/global.scss','project/static/css/dev/**/*.scss'],
  images: 'project/static/img/**/*.{png,jpg,gif,jpeg}'
};

gulp.task('sass', function () {
  gulp.src(paths.css)
    .pipe(sass())
    .pipe(minifyCSS({keepBreaks:false}))
    .pipe(concat('all.min.css'))
    .pipe(gulp.dest('project/static/css/build'));
});

gulp.task('clean', function(cb) {
  del(['build'], cb);
});

gulp.task('browserify', function() {
  gulp.src('react/main.react.jsx')
  .pipe(browserify({transform: 'reactify'}))
  .pipe(concat('react-bundle.js'))
  //.pipe(uglify())
  .pipe(gulp.dest('project/static/js/build'));
});

gulp.task('scripts', ['clean'], function() {
  // Minify and copy all JavaScript (except vendor scripts)
  return gulp.src(paths.scripts)
    .pipe(uglify())
    .pipe(concat('all.min.js'))
    .pipe(gulp.dest('project/static/js/build'));
});

gulp.task('images', ['clean'], function() {
 return gulp.src(paths.images)
    .pipe(imagemin({optimizationLevel: 5}))
    .pipe(gulp.dest('project/static/img'));
});

gulp.task('watch', function() {
  gulp.watch(paths.css, ['sass']);
  gulp.watch(paths.scripts, ['scripts']);
  gulp.watch(['react/**/*.*'], ['browserify']);
});

gulp.task('default', ['watch', 'scripts', 'images','sass', 'browserify']);
