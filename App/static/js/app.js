/**
 * app.js: 
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
    const inputEmail = document.getElementById("inputEmail");
    const inputPassword = document.getElementById("inputPassword");
    const btnLogin = document.getElementById("btnLogin");
    const btnSingIn = document.getElementById("btnSingIn");
    const btnSingOut = document.getElementById("btnSingOut");
    const btnFacebookSingIn = document.getElementById("btnFacebookSingIn");
    const btnGoogleSingIn = document.getElementById("btnGoogleSingIn");


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
                    alert('Wrong password.');
                } else {
                    alert(errorMessage);
                }
                console.log(error);
            });

    });

    //TODO : 
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


    //Boton Facebook
    btnFacebookSingIn.addEventListener('click', e => {
        alert("Facebook");
        console.log("Facebook")
        var provider = new firebase.auth.FacebookAuthProvider();

        //firebase.auth().signInWithRedirect(provider);

        firebase.auth().signInWithPopup(provider).then(function(result) {
            // This gives you a Google Access Token. You can use it to access the Google API.
            var token = result.credential.accessToken;
            // The signed-in user info.
            var user = result.user;
            // ...
        }).catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            // The email of the user's account used.
            var email = error.email;
            // The firebase.auth.AuthCredential type that was used.
            var credential = error.credential;
            // ...
        });
    });

    //Boton Google
    btnGoogleSingIn.addEventListener('click', e => {
        alert("Google");
        console.log("Google")
        var provider = new firebase.auth.GoogleAuthProvider();

        //firebase.auth().signInWithRedirect(provider);
        firebase.auth().signInWithPopup(provider).then(function(result) {
            // This gives you a Google Access Token. You can use it to access the Google API.
            var token = result.credential.accessToken;
            // The signed-in user info.
            var user = result.user;
            // ...
        }).catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            // The email of the user's account used.
            var email = error.email;
            // The firebase.auth.AuthCredential type that was used.
            var credential = error.credential;
            // ...
        });

    });

    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            // User is signed in.
            var displayName = user.displayName;
            var email = user.email;
            var emailVerified = user.emailVerified;
            var photoURL = user.photoURL;
            var isAnonymous = user.isAnonymous;
            var uid = user.uid;
            var providerData = user.providerData;

            console.log("change if", user);
        } else {
            console.log("change else", user);
        }
    });

    //Actualiza usuario al backend 
    updateBackend = (pUuser, pPass) => {
        //TODO:
        /**
         * actualizar usario en el backend
         */
    }

})();