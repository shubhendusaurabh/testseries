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
                        processQuestions();
                        deferred.resolve(questions);
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

        function processQuestions() {
          for (var i = 0; i < questions.length; i++) {
            questions[i].viewed = false;
            questions[i].saved = false;
            questions[i].review = false;
          }
        }

        function setStateToTrue(id, property) {
          questions[id].property = true;
        }

        function getQuestionById(id) {
            var deferred = $q.defer();
            if (questions != null && questions[id]) {
                questions[id].viewed = true;
                console.log("set to true");
                deferred.resolve(questions[id]);
            } else {
                getAllQuestions().then(function () {
                  questions[id].viewed = true;
                  console.log(questions);
                  deferred.resolve(questions[id]);
                });
            }
            return deferred.promise;
        }

        return {
            getAllQuestions: getAllQuestions,
            getQuestionById: getQuestionById,
            setStateToTrue: setStateToTrue
        }
    }
]);
