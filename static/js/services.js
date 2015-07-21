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
            questions[i].status = 'not_answered';
          }
        }

        function setStatus(id, status) {
          questions[id].status = status;
        }

        function getQuestionById(id) {
            var deferred = $q.defer();
            if (questions[id]) {
              setStatus(id, "viewed");
              deferred.resolve(questions[id]);
            } else {
              deferred.reject("Not found");
            }
            return deferred.promise;
        }

        return {
            getAllQuestions: getAllQuestions,
            getQuestionById: getQuestionById,
            setStatus: setStatus
        }
    }
]);
