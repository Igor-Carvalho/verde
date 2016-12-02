(function () {
  'use strict';

  angular.module('verde')
    .factory('contatoFormService', ['$http', 'contatoFormAction', contactFormService]);

  function contactFormService($http, contatoFormAction) {
    return {
      sendMessage: function (message) {
        return $http.post(contatoFormAction, message)
      }
    }
  }
})();
