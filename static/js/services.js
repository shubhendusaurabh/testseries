'use strict';

var questionsService = angular.module('Questions.services', []);

questionsService.factory('QuestionService', ['$http', '$q',
    function ($http, $q) {

        var questions = null;

        function getAllQuestions() {
            var deferred = $q.defer();
            if (questions == null) {
                $http.get('/api/questions/')
                    .success(function (data) {
                        questions = data.results;
                        deferred.resolve(data.results);
                    })
                    .error(function (error) {
                        console.error(error);
                        deferred.reject(error)
                    });
            } else {
                deferred.resolve(questions);
            }
            return deferred.promise;
        }

        function getQuestionById(id) {
            var deferred = $q.defer();
            if (questions != null && questions[id]) {
                deferred.resolve(questions[id]);
            } else {
                getAllQuestions().then(function () {
                    deferred.resolve(questions[id]);
                });
            }
            return deferred.promise;
        }

        return {
            getAllQuestions: getAllQuestions,
            getQuestionById: getQuestionById
        }
    }
]);
