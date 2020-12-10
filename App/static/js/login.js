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

    const ADMIN_PATH = "/";
    const CLIENT_PATH = "/cliente"
    const ADMIN_ROL_ID = 1
    const CLIENT_ROL_ID = 2
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
        //Boton Facebook
    btnFacebookSingIn.addEventListener('click', e => {
        console.log("Facebook")
        var provider = new firebase.auth.FacebookAuthProvider();

        //firebase.auth().signInWithRedirect(provider);

        firebase.auth().signInWithPopup(provider).then(function(result) {
            console.log(result);
        }).catch(function(error) {
            console.log(error);
        });
    });


    //Boton Google
    btnGoogleSingIn.addEventListener('click', e => {
        console.log("Google")
        var provider = new firebase.auth.GoogleAuthProvider();

        //firebase.auth().signInWithRedirect(provider);
        firebase.auth().signInWithPopup(provider).then(function(result) {
            console.log(result);
        }).catch(function(error) {
            console.log(error);
        });
    });

    /*
    const validateUserRol = (user) => {
        let url = window.location.href + "/validarRolUsuario?usuario=" + user;
        let userData = { "user": user };
        fetch(url)
            .then(
                function(response) {
                    if (response.status !== 200) {
                        console.log('estado de error: ' +
                            response.status);
                        return;
                    }
                    // Examine the text in the response
                    response.json().then(function(data) {
                        console.log(data);
                        if (data.rol_id === ADMIN_ROL_ID) {
                            location.href = ADMIN_PATH;
                        } else if (data.rol_id === CLIENT_ROL_ID) {
                            location.href = CLIENT_PATH;
                        } else {
                            console.log("Rol ID", data.rol_id); //el id no es cliente ni admin

                            //debe REGISTRAR el usuario
                            //DEBE hacer redireccion a cliente porque es nuevo 

                        }
                    });
                }
            )
            .catch(function(err) {
                console.log('Fetch Error :-S', err);
            });
    }
*/

    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            //validateUserRol(user.email); // Valida rol y redirecciona --> se podria reducir compelgidad 
            console.log("Login", user.mail);
        } else {
            console.log("change else", user);
            /*  if (location.pathname !== "/login") {
                 location.href = "/login";
             } */
        }
    });


    //Actualiza usuario al backend 
    //VER SI ME COVIENE USASR SESSION STORAGE:
    //https://developer.mozilla.org/es/docs/Web/API/Window/sessionStorage

    const updateBackend = async(user, password) => {
        //TO DO 
        /**
         * mandar al backen el nuevo usuario para agregarlo
         * debe validar si existe. 
         * 
         * 
         */
        //let usuarui_actual = sessionStorage.getItem('user');
        let url = "";
        let userData = { "user": user, "password": password };
        let res = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(userData),
            headers: {
                'Content-Type': 'application/json'
            }
        });

    }




    //====================================no se va a usar
    const addStoreLocalUserLogin = (pUuser) => {
        //TODO
        sessionStorage.setItem('user', pUuser);

    }

    let deleteStoreLocalUserLogin = (pUuser) => {
        //TODO
        //sessionStorage.setItem('user', pUuser);

        sessionStorage.removeItem('user');
    }

    //NUEVA PANTALLA
    //VALIDAR SI HAY USUARIO LOGUEADO, DESDE SESSIONSTORAGE 
    //OK : PASA Y MUESTA PAGINA 
    //NO OK : REDIRECCIONA A LOGIN 

})();