/**
 * login.js: 
 * gentiona pantalla de login 
 * permite autnticacion con redes sociales e email
 * 
 * 
 */

//Se carga inmediatemente despues de ser creada 

(function() {

    //Configura app Firebase
    var firebaseConfig = {
        apiKey: "AIzaSyBHoVNC2ji7XihvnD22q9SysNl9OGlDapc",
        authDomain: "apptaller2019.firebaseapp.com",
        databaseURL: "https://apptaller2019.firebaseio.com",
        projectId: "apptaller2019",
        storageBucket: "apptaller2019.appspot.com",
        messagingSenderId: "171601985099",
        appId: "1:171601985099:web:fcba3f334a55c6bc6997ce"
    };
    //Inicializa App Firebase 
    firebase.initializeApp(firebaseConfig);

    //Vincular elementos del DOM
    /*
    const inputEmail = document.getElementById("inputEmail");
    const inputPassword = document.getElementById("inputPassword");
    const btnLogin = document.getElementById("btnLogin");
    const btnSingIn = document.getElementById("btnSingIn");
    const btnSingOut = document.getElementById("btnSingOut");
    */
    const btnFacebookSingIn = document.getElementById("btnFacebookSingIn");
    const btnGoogleSingIn = document.getElementById("btnGoogleSingIn");

    //const ADMIN_PATH = "/";
    //const CLIENT_PATH = "/cliente"
    //const ADMIN_ROL_ID = 1
    //const CLIENT_ROL_ID = 2
    /*
        //Clic boton Login 
        btnLogin.addEventListener('click', e => {
            //obtenego valor de los inputs
            const email = inputEmail.value;
            const password = inputPassword.value;

            const auth = firebase.auth();
            auth.signInWithEmailAndPassword(email, password)
                .then(function(e) {
                    console.log("usuario logueado", e);
                })
                .catch(function(error) {
                    // Handle Errors here.
                    var errorCode = error.code;
                    var errorMessage = error.message;
                    console.log(errorCode, errorMessage);

                    if (errorCode === 'auth/wrong-password') {
                        alert('Contraseña incorrecta!!!');
                    } else if (errorCode === 'auth/invalid-email') {
                        alert('Debe ingresar un Email de Ususario ya registrado valido!!!');
                    }
                    console.log(error);
                });

        });


        //boton Sing in (crear usuario)
        btnSingIn.addEventListener('click', e => {
            //obtenego valor de los inputs
            const email = inputEmail.value;
            const password = inputPassword.value;

            const auth = firebase.auth();
            auth.createUserWithEmailAndPassword(email, password).catch(function(error) {
                // Handle Errors here.
                var errorCode = error.code;
                var errorMessage = error.message;
                console.log("error cear usuario", errorCode, errorMessage);
            });
        });


        //boton Sing out 
        btnSingOut.addEventListener('click', e => {
            const auth = firebase.auth();
            auth.signOut().then(function() {
                // Sign-out successful.
            }).catch(function(e) {
                // An error happened.
                console.log(e);
            });
        });

    */

    let CosultarUsuarioBackend = (usuario) => {
        // se Arma la url para validar el usuario contra el backend
        let url = window.location.origin + "/validarSignInRedes";
        //Se arma el json para enviar el email del usuario al backend
        let userData = { "email": usuario }

        //Se hace la consulta al backend 
        let res = fetch(url, {
            method: 'POST',
            body: JSON.stringify(userData),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((response) => {
            console.log(response);

            response.json().then(data => {
                console.log('data', data);

                if (data.usuario_regitrado === true) { //el usario esta regitrado en el backend 
                    console.log("Redirigir al inicio con la sesion guardada en el backend");
                    location.href = '/'; //Redirecciona al inicio 
                } else { //usuario no regitrado en el Backend
                    console.log("Redirección a registro de usuario");
                    location.href = "/altaUsuario"; //redirecciona al Alta de usuario
                }

            });

        }).catch((error) => {
            console.log(error);
        });
    }





    //Boton Google
    btnGoogleSingIn.addEventListener('click', e => {
        console.log("Google")
        var provider = new firebase.auth.GoogleAuthProvider();

        //firebase.auth().signInWithRedirect(provider);
        firebase.auth().signInWithPopup(provider).then(function(result) {
            console.log(result);
            console.log('usuario Google:', result.user.email);
            console.log(result.operationType);

            //CONSULTA AL BACKEND POR EL USUARIO
            CosultarUsuarioBackend(result.user.email);


        }).catch(function(error) {
            console.log(error);
            //Si el usario cierra el la ventana emergente de red social 
            if (error.code == "auth/popup-closed-by-user") {
                alert('Ha cerrado el login de Red Social!!!')
            }

        });
    });


    //Boton Facebook
    btnFacebookSingIn.addEventListener('click', e => {
        console.log("Facebook")
        var provider = new firebase.auth.FacebookAuthProvider();

        //firebase.auth().signInWithRedirect(provider);

        firebase.auth().signInWithPopup(provider).then(function(result) {
            console.log(result);
            console.log('usuario Facebook:', result.user.email);
            console.log(result.operationType);

            //CONSULTA AL BACKEND POR EL USUARIO
            CosultarUsuarioBackend(result.user.email);


        }).catch(function(error) {
            console.log(error);
            //Si el usario cierra el la ventana emergente de red social 
            if (error.code == "auth/popup-closed-by-user") {
                alert('Ha cerrado el login de Red Social!!!')
            }

        });
    });



    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            //validateUserRol(user.email); // Valida rol y redirecciona --> se podria reducir compelgidad 
            console.log("LoginRedes usuario logueado", user.email);


            //window.location.href = window.location;
        } else {
            console.log("no Logueado", user);
            /*  if (location.pathname !== "/loginRedes") {
                 location.href = "/loginRedes";
             } */
        }
    });





})();