/**(function() {

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

        //let body = document.getElementsByTagName("body")[0]
        // body.style.visibility = "hidden";

        //Armar un cargando o algo  
        /*
            firebase.auth().onAuthStateChanged(function(user) {
                if (user) {
                    console.log("Logueado/cargado en red social firebase", user);
                    //body.style.visibility = ""; //muetra la admin solo si esta logueado
                } else {
                    console.log("No loguedo", user);

                    // if (location.pathname !== "/loginRedes")
                    // location.href = "/loginRedes";
                }
            });



        })();
        */
/*
const btnSingOut = document.getElementById("btnSingOut");

btnSingOut.addEventListener('click', e => {
    //alert('Esta salindo de la app... Chau! ')

    let res = confirm("¿Desea salir?");
    if (res) {
        const auth = firebase.auth();
        auth.signOut().then(function() {
            // Sign-out successful.
        }).catch(function(e) {
            // An error happened.
            console.log(e);
        });
    }


});
*/