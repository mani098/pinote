app = angular.module('pinoteApp', ['LocalStorageModule']).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;';
});

app.controller('pinoteController', ['$scope', '$http','localStorageService', function($scope, $http, localStorageService) {
	var self = this;
	$scope.init = function () {
		self.pinote_module = 'Passvault';
		$scope.passvaultData();
		if(localStorageService.isSupported) {
			if (localStorageService.get('username')) {
				self.username = localStorageService.get('username');
			}
			else {
				$http.get('/get-user/').success(function(response) {
					self.username = response;
					localStorageService.set('username', self.username);
				});
			}
		}
	};
	$scope.passvaultData = function() {
		$http.get('/passvault/').success(function(response) {
			self.passvault_datas = response;
			$scope.clear_weblinks();
			self.pinote_module = 'Passvault';
			});
	};
	$scope.weblinksData = function() {
		$http.get('/weblinks/').success(function(response) {
			self.weblinks_datas = response;
			$scope.clear_passvault();
			self.pinote_module = 'Weblinks';
		});
	};
	$scope.load_passvault_data = function(category, category_data) {
		$scope.passvault_category = category;
		$scope.passvault_fields = category_data;
	};
	$scope.update_passvault = function(passvaultpost, passvault_category, custom_rows) {
		// Make Server POST request with JSON object

		// if (passvaultpost["custom_fields"])	passvaultpost["custom_fields"] = passvaultpost["custom_fields"].concat(custom_rows);
		// else passvaultpost["custom_fields"] = custom_rows;
		post_data = {
			"id": passvaultpost["id"],
			"name": passvaultpost["name"],
			"password": passvaultpost["password"],
			"category": passvault_category,
			"custom_fields": angular.toJson(passvaultpost["custom_fields"]),
			"description": passvaultpost["description"]
		};
		console.log(post_data);
		$http.post('/passvault/updatedata/', $.param(post_data)).
			success(function(data, status, headers, config) {
				console.log("data saved");
				$scope.passvaultData();
			});
	}
	$scope.clearCache = function() {
		localStorageService.clearAll();
	};
	$scope.clear_passvault = function() {
		self.passvault_datas = null;
		$scope.passvault_fields = null;
	};
	$scope.clear_weblinks = function() {
		self.weblinks_datas = null;
	};
	$scope.spaceless = function(input) {
		if (input) {
			return input.replace(/\s+/g, '-');
		}
	}
	$scope.add_field = function(field_name, field_value, passvault_fields) {
		// passvault_fields = passvault_fields.concat({field_name:field_value});
		console.log(passvault_fields);
	}

}]);
