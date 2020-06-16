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

    //salir
    /*  const btnSingOut = document.getElementById("btnSingOut");

     btnSingOut.addEventListener('click', e => {
         alert('ghjgj')
         const auth = firebase.auth();
         auth.signOut().then(function() {
             // Sign-out successful.
         }).catch(function(e) {
             // An error happened.
             console.log(e);
         });
     }); */

    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
            // User is signed in.
            /*             var displayName = user.displayName;
                        var email = user.email;
                        var emailVerified = user.emailVerified;
                        var photoURL = user.photoURL;
                        var isAnonymous = user.isAnonymous;
                        var uid = user.uid;
                        var providerData = user.providerData; */

            console.log("Logueado", user);
            //if (location.pathname !== "/")
            //    location.href = "/";

        } else {
            console.log("No loguado", user);

            if (location.pathname !== "/login")
                location.href = "/login";
        }
    });



})();

const btnSingOut = document.getElementById("btnSingOut");

btnSingOut.addEventListener('click', e => {
    alert('Esta salindo de la app!!!')
    const auth = firebase.auth();
    auth.signOut().then(function() {
        // Sign-out successful.
    }).catch(function(e) {
        // An error happened.
        console.log(e);
    });
});