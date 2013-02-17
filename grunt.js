"use strict";
module.exports = function(grunt) {

    process.env.NODE_ENV = "test";

    // Add our custom tasks.
 //   grunt.loadNpmTasks("grunt-coffeelint");

    // https://github.com/pghalliday/grunt-mocha-test
//    grunt.loadNpmTasks("grunt-mocha-test");


    // Project configuration.
    grunt.initConfig({
        coffeelint: {
            app: ["coffee/**/*"]
        },

        coffeelintOptions: {},

        mochaTest: {
            files: []
        },
        mochaTestConfig: {},

        watch: {
        }

    });

    // Default task
    grunt.registerTask("default", "lint test");
    grunt.registerTask("test", "mochaTest");

    grunt.registerTask("lint", "coffeelint"):
};

