var app = angular.module("ticketsyApp", []);
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{_');
        $interpolateProvider.endSymbol('_}');
    });

function controller($scope, $http) {

    $scope.usuarios = []
    $http.get('/admin/rest/listar').success(function(json){
        $scope.usuarios = json;
    })

    $scope.editarUsuario = function(usuario) {
        usuario.editando = true;
    }

    $scope.salvarUsuario = function() {

        var usuario = {
            "firstname": $scope.inputFirstName,
            "lastname": $scope.inputLastName,
            "sex": $scope.inputGender,
            "country": $scope.inputCountry,
            "state": $scope.inputState,
            "city": $scope.inputCity,
            "address": $scope.inputAddress,
            "zipcode": $scope.inputZipCode,
            "phone": $scope.inputPhone,
            "email": $scope.inputEmail
        };
        console.log(usuario)
        $http.post('/admin/rest/salvar', usuario).success(function(json){

            usuario.id = json.id;
            usuario.editando = false;
            $scope.usuarios.push(usuario)

            $scope.inputFirstName = "";
            $scope.inputLastName = "";
            $scope.inputGender = "";
            $scope.inputCountry = "";
            $scope.inputState = "";
            $scope.inputCity = "";
            $scope.inputAddress = "";
            $scope.inputZipCode = "";
            $scope.inputPhone = "";
            $scope.inputEmail = "";

        });

    }

    $scope.confirmarEdicao = function(usuario){
        usuario.editando = false;

        params = {"idUsuario": usuario.id,
                    "firstname": usuario.firstname,
                    "lastname": usuario.lastname,
                    "sex": usuario.sex,
                    "country": usuario.country,
                    "state": usuario.state,
                    "city": usuario.city,
                    "address": usuario.address,
                    "zipcode": usuario.zipcode,
                    "phone": usuario.phone,
                    "email": usuario.email
        }

        $http.post('/admin/rest/editar', params);

    }

    $scope.removerElemento = function(usuario, index){
        $scope.usuarios.splice(index, 1);
        usuario.editando = false;

        $http.post('/admin/rest/remover', {"idUsuario": usuario.id});
    }

    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };

    $scope.addUser = function(){
        $scope.usuarios.push({'firstname': $scope.inputFirstName, 'lastname': $scope.inputLastName,'email': $scope.inputEmail})
        users_service.addUser($scope.inputFirstName, $scope.inputLastName, $scope.inputEmail)
    }

}