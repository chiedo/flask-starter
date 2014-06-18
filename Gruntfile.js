module.exports = function(grunt) {
  grunt.initConfig({
   nose: {
     options: {
      verbosity: 2, 
      rednose: true
     },
     src: ['./'] 
    },
 
    watch: {
      js: {
        options: {
          spawn: true,
          interrupt: true,
          debounceDelay: 250,
        },
        files: ['Gruntfile.js', '*.py', '**/*.py'],
        tasks: ['nose']
     }
    }
  });
 
  grunt.loadNpmTasks('grunt-nose');
  grunt.loadNpmTasks('grunt-contrib-watch');
 
  grunt.registerTask('default', ['nose']);
};
