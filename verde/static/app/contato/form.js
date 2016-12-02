(function () {
  'use strict';

  angular.module('verde').component('contatoForm', {
    templateUrl: ['contatoForm', function (contatoForm) { return contatoForm; }],
    controllerAs: 'vm',
    controller: ['contatoFormService', controller]
  });

  function controller(contatoFormService) {
    var self = this;
    self.message = {};
    self.count = 1;

    self.sendMessage = sendMessage;

    function sendMessage(contactForm) {
      self.promise = contatoFormService.sendMessage(self.message);
      self.promise.then(success, error);

      function success() {
        self.error_message = false;
        self.success_message = true;
        self.message = {};
        self.count++;
        contactForm.$setPristine();
      }

      function error() {
        self.success_message = false;
        self.error_message = true;
      }
    }
  }
})();
