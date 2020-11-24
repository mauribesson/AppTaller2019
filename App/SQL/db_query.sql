/*
 * agregar : 
 -- insertar datos que se necesitan para arrancar..
*/

CREATE TABLE "rol" (
	"idRol" serial NOT NULL,
	"nombreRol" character varying (30) NOT NULL,
	Primary Key ("idRol")
);

CREATE TABLE "usuario" (
	"nombre" character varying(30) NOT NULL,
	"contrasenia" character varying (20) NOT NULL, 
	"contacto" character varying (70),
	"rol" smallint NOT NULL,
	Primary Key ("nombre"),
	foreign key ("rol") references "rol" deferrable
);

---CARGA DE USUARIOS
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('Mario@aaa', '123', 'etrada 10030', 1); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('andreaabrigo@gmail.com', '123456789', 'Andrea', 1); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('andrea@gmail.com', '1234', 'andrea@gmail.com', 2); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('estebanl@gmail.com', 'narciso45', '15497875', 2); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('perezh@gmail.com', 'horacio1979', 'Sanders 779', 2); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('emet@gmail.com', 'emetraul', 'Rocamora 1181', 2); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('chinaramirez@gmail.com', 'china2020', '15872571 ', 2); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('scott1990@gmail.com', '123456789', 'Estrada 1949', 2); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('nicktower@gmail.com', 'nick1234', 'Cazadores 231', 2); 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('rosamartineza@gmail.com', 'rosemarie', '15560350 ', 2); 


CREATE TABLE "tipoProducto" (
	"idTipo" serial NOT NULL,
	"nombreTipo" character varying(30) NOT NULL,
	Primary key ("idTipo")
);

---CARGA DE TIPOS DE PRODUCTOS
--INSERT INTO "tipoProducto" ("nombreTipo") values ('mouse'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('teclado'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('monitor'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('cpu'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('auriculares'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('parlantes'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('webcam'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('joystick'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('memoria'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('bateria'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('cable'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('cargador'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('cartucho'); 
--INSERT INTO "tipoProducto" ("nombreTipo") values ('disco');
--INSERT INTO "tipoProducto" ("nombreTipo") values ('fuente');
--INSERT INTO "tipoProducto" ("nombreTipo") values ('gabinete');
--INSERT INTO "tipoProducto" ("nombreTipo") values ('grabadora');
--INSERT INTO "tipoProducto" ("nombreTipo") values ('imporesora');
--INSERT INTO "tipoProducto" ("nombreTipo") values ('placa');
--INSERT INTO "tipoProducto" ("nombreTipo") values ('ups');
--INSERT INTO "tipoProducto" ("nombreTipo") values ('ventilador');
--INSERT INTO "tipoProducto" ("nombreTipo") values ('Notebook');

CREATE TABLE "marca" (
	"idMarca" serial NOT NULL,
	"nombre" character varying(30) NOT NULL,
	Primary key ("idMarca")
);

---CARGA DE MARCAS
--INSERT INTO "marca" ("nombre") values ('Bangho');
--INSERT INTO "marca" ("nombre") values ('Compaq');
--INSERT INTO "marca" ("nombre") values ('Benq');
--INSERT INTO "marca" ("nombre") values ('Acer');
--INSERT INTO "marca" ("nombre") values ('Samsung');
--INSERT INTO "marca" ("nombre") values ('Nikon');
--INSERT INTO "marca" ("nombre") values ('Canon');
--INSERT INTO "marca" ("nombre") values ('Epson');
--INSERT INTO "marca" ("nombre") values ('Bangho');
--INSERT INTO "marca" ("nombre") values ('Hewlett Packard');
--INSERT INTO "marca" ("nombre") values ('Intel');
--INSERT INTO "marca" ("nombre") values ('Biostar');
--INSERT INTO "marca" ("nombre") values ('Kingston');
--INSERT INTO "marca" ("nombre") values ('GoldRam');
--INSERT INTO "marca" ("nombre") values ('Western Digital');
--INSERT INTO "marca" ("nombre") values ('Seagate');
--INSERT INTO "marca" ("nombre") values ('Maxtor');
--INSERT INTO "marca" ("nombre") values ('Hitachi');
--INSERT INTO "marca" ("nombre") values ('IOmega');
--INSERT INTO "marca" ("nombre") values ('Genius');
--INSERT INTO "marca" ("nombre") values ('Sony');
--INSERT INTO "marca" ("nombre") values ('D-link');
--INSERT INTO "marca" ("nombre") values ('SMC');
--INSERT INTO "marca" ("nombre") values ('Energit');
--INSERT INTO "marca" ("nombre") values ('Philips');
--INSERT INTO "marca" ("nombre") values ('Platinium');
--INSERT INTO "marca" ("nombre") values ('LG');
--INSERT INTO "marca" ("nombre") values ('Logitech');

CREATE TABLE "producto" (
	"id" serial NOT NULL,
	"nombre" character varying (30) NOT NULL,
	"descripcion" character varying (150) NOT NULL,
	"precio" float NOT NULL,
	"modelo" character varying (30),
	"garantia" smallint,
	"tipoProducto" smallint,
	"marca" smallint,
	Primary key ("id"),
	foreign key ("tipoProducto") references "tipoProducto" deferrable,
	foreign key ("marca") references "marca" deferrable
);

--- CARGA DE PRODUCTOS
--- ATENCION CAMBIAR LOS ID DEL TIPO DE PRODUCTO Y DE LA MARCA
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Monitor Led Philips', 'Monitor Led 18.5 pulgadas con SmartControl Lite', 7500, 'Philips P2', 12, 29, 52);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Disco duro portatil', 'Disco duro portatil', 5800, '42wd', 12, 40, 41);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Mouse inalambrigo Genius', 'Mouse inalámbrigo Genius modelo NX-7000 2.4 GHz de radio frecuencia 1200 dpi de resolucion del sensor', 900, 'NX-7000', 6, 27, 46);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Auriculares inalambricos Sony', 'Conexion mediante Bluetooh. Su enlace inalámbrico es de 10m. Su batería dura 35 horas. Con micrófono incorporado', 5000, 'WH-CH510', 12, 31, 48);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Impresora Epson XP-211', 'Impresora inalámbrica con escaner y copiadora. Utiiza cartuchos individuales. Imprime hasta 27 ppm3 en texto negro y 15 ppm3 en texto a color', 16000, 'XP-211', 24, 44, 35);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Teclado Genius', 'Forma de las teclas: cilíndrica. Tipo de conector: USB. Peso: 450g. Medidas de 139.67mm de alto, 440.51mm de ancho y 20.07mm de profundidad.', 755, 'Smart KB-100', 6, 28, 46);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Parlantes Genius', 'Descripción: Genius SP-Q160 ofrece un sonido natural, con una gran claridad y precisión, que se dispersa uniformemente por toda la habitación. Un parlante que aseg', 1370, 'SP-Q160', 9, 32, 46);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Joystick inalámbrico Sony', 'Inalámbrico. Largo x Ancho x Altura: 92.2 mm x 141.22 mm x 215.9 mm', 2240, 'Dualshock 3', 12, 34, 49);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Cable micro usb', 'Largo del cable: 1.5 m. Velocidad máxima de transferencia de datos: 60 MB/s', 210, 'JA109', 3, 37, 39);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Cable micro usb', 'Largo del cable: 1.5 m. Velocidad máxima de transferencia de datos: 60 MB/s', 210, 'JA109', 3, 37, 39);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Disco rigido', 'Capacidad 1024 GB. Velocidad 7200 rpm. Peso 0.45 g. Cache 64 MB', 5380, 'WD10EZEX', 18, 40, 41);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Impresora multifunción', 'Wifi. USB. Velocidad del procesador: 360 MHz Velocidad de impresión en blanco y negro: 8 ppm Velocidad de impresión en color: 5 ppm', 19725, '415', 12, 44, 36);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Notebook Bangho', 'Procesador: Procesador Intel Celeron N4020, caché de 4 MB, hasta 2,80 GHz Memoria: 4GB DDR4 Almacenamiento: 240GB M.2', 45000, 'L4 i1', 24, 49, 28);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Mouse Logitech', 'Con cable. Alcance máximo: 2.1 m. Sensor óptico. Con luces.', 1200, 'Prodigy', 9, 27, 55);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Teclado Logitech', 'Arquitectura: Membrana. Largo del cable: 1.5 m.  Tipo de conector: USB', 1500, 'K120', 12, 28, 55);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Monitor Acer', 'Pantalla Led. Tamaño 19.5". Resolución 1600px-900px. Tipos de conexión: VGA, HDMI.', 13500, 'V206HQL', 24, 29, 31);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('CPU Intel', '16 GIGAS MEMORIA RAM DISCO RIGIDO 1 TERA GAB ATX 500W', 53000, 'core i 7 intel XEON', 24, 30, 37);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Auriculares Samsung', 'Longitud del cable: 1,2 m. Peso: 11,2 g. Con micrófono. Formato del auricular: In-ear.', 800, 'YJ', 3, 31, 32);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Parlantes HP', '2 parlantes para pc. Tipos de filtros del parlante: 2.0', 2350, 'UC230', 6, 32, 36);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Webcam Philips', 'Con micrófono incorporado. Resolución de imagen: 2 Mpx. Resolución de imagen: 2 Mpx', 5800, 'spg9406', 18, 33, 52);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Joystick Logitech', 'Inalámbrico. Tipo de control: Gamepad.', 5400, 'F710', 12, 34, 55);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Memoria RAM 8GB', 'Tecnología: DDR4 SDRAM. Velocidad: 2400 MHz. Cantidad de pines: 288', 3700, 'KVR24N17S8/8', 6, 35, 39);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Memoria RAM 4GB', 'Tecnología: DDR3 SDRAM. Velocidad: 1600 MHz. Cantidad de pines: 240', 2500, 'KVR16N11S8/4', 6, 35, 39);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Memoria RAM 2GB', 'Tecnología: DDR3 SDRAM. Velocidad: 1333 MHz. Cantidad de pines: 288', 1800, 'KVR1333D3N9/2G', 6, 35, 39);
--INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
--values ('Cable HDMI Sony', 'Largo del cable: 2 m. Cantidad de conectores de salida: 1 y de entrada 1', 2500, '3dt2', 6, 37, 48);


CREATE TABLE "imagenes" (
	"id" serial NOT NULL,
	"idProducto" smallint NOT NULL,
	"urlImagen" character varying (500) NOT NULL,
	Primary key ("id"),
	foreign key ("idProducto") references "producto" deferrable
);

--- CARGA DE IMAGENES DE PRODUCTOS
--- ATENCION CAMBIAR LOS ID DEL TIPO DE PRODUCTO
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (8, 'https://storage.googleapis.com/apptaller-18740.appspot.com/monitor-led2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (8, 'https://storage.googleapis.com/apptaller-18740.appspot.com/monitor-led.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (10, 'https://storage.googleapis.com/apptaller-18740.appspot.com/discorigido.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (10, 'https://storage.googleapis.com/apptaller-18740.appspot.com/discorigido1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (11, 'https://storage.googleapis.com/apptaller-18740.appspot.com/mouse1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (11, 'https://storage.googleapis.com/apptaller-18740.appspot.com/mouse2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (12, 'https://storage.googleapis.com/apptaller-18740.appspot.com/auricularSony1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (12, 'https://storage.googleapis.com/apptaller-18740.appspot.com/auricularSony2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (13, 'https://storage.googleapis.com/apptaller-18740.appspot.com/impresoraEpsonXP211.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (13, 'https://storage.googleapis.com/apptaller-18740.appspot.com/impresoraEpsonXP211-2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (14, 'https://storage.googleapis.com/apptaller-18740.appspot.com/tecladoGenius1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (14, 'https://storage.googleapis.com/apptaller-18740.appspot.com/tecladoGenius2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (15, 'https://storage.googleapis.com/apptaller-18740.appspot.com/parlantegenius1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (15, 'https://storage.googleapis.com/apptaller-18740.appspot.com/parlantegenius2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (15, 'https://storage.googleapis.com/apptaller-18740.appspot.com/parlantegenius3.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (16, 'https://storage.googleapis.com/apptaller-18740.appspot.com/joystick1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (16, 'https://storage.googleapis.com/apptaller-18740.appspot.com/joystick2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (17, 'https://storage.googleapis.com/apptaller-18740.appspot.com/cableusb.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (17, 'https://storage.googleapis.com/apptaller-18740.appspot.com/cableusb2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (18, 'https://storage.googleapis.com/apptaller-18740.appspot.com/discorigido1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (18, 'https://storage.googleapis.com/apptaller-18740.appspot.com/discorigido2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (19, 'https://storage.googleapis.com/apptaller-18740.appspot.com/impresora1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (19, 'https://storage.googleapis.com/apptaller-18740.appspot.com/impresora2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (20, 'https://storage.googleapis.com/apptaller-18740.appspot.com/pcbangho1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (20, 'https://storage.googleapis.com/apptaller-18740.appspot.com/pcbangho2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (21, 'https://storage.googleapis.com/apptaller-18740.appspot.com/mouseLogitech1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (21, 'https://storage.googleapis.com/apptaller-18740.appspot.com/mouseLogitech2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (22, 'https://storage.googleapis.com/apptaller-18740.appspot.com/tecladoLogitech.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (22, 'https://storage.googleapis.com/apptaller-18740.appspot.com/tecladoLogitech2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (23, 'https://storage.googleapis.com/apptaller-18740.appspot.com/monitorAcer1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (23, 'https://storage.googleapis.com/apptaller-18740.appspot.com/monitorAcer2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (24, 'https://storage.googleapis.com/apptaller-18740.appspot.com/cpuintel1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (25, 'https://storage.googleapis.com/apptaller-18740.appspot.com/auricularessamsung1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (25, 'https://storage.googleapis.com/apptaller-18740.appspot.com/auricularessamsung2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (26, 'https://storage.googleapis.com/apptaller-18740.appspot.com/parlantesHP1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (27, 'https://storage.googleapis.com/apptaller-18740.appspot.com/webcamphilips1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (27, 'https://storage.googleapis.com/apptaller-18740.appspot.com/webcamphilips2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (28, 'https://storage.googleapis.com/apptaller-18740.appspot.com/joystickLogitech1.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (28, 'https://storage.googleapis.com/apptaller-18740.appspot.com/joystickLogitech2.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (29, 'https://storage.googleapis.com/apptaller-18740.appspot.com/memoria.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (30, 'https://storage.googleapis.com/apptaller-18740.appspot.com/memoria.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (31, 'https://storage.googleapis.com/apptaller-18740.appspot.com/memoria.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (32, 'https://storage.googleapis.com/apptaller-18740.appspot.com/cablehdmiSony.jpg');
--INSERT INTO "imagenes"("idProducto", "urlImagen")
--values (32, 'https://storage.googleapis.com/apptaller-18740.appspot.com/cablehdmiSony2.jpg');

CREATE TABLE "ejemplar" (
	"numeroSerie" character varying(50) NOT NULL,
	"vendido" boolean NOT NULL,
	"producto" smallint NOT NULL,
	Primary key ("numeroSerie"),
	foreign key ("producto") references "producto" deferrable
);

--- CARGA DE EJEMPLARES DE PRODUCTOS
--- ATENCION CAMBIAR LOS ID DEL PRODUCTO
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MLP01', 'false', 8);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MLP02', 'false', 8);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MLP03', 'false', 8);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MLP04', 'false', 8);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MLP05', 'false', 8);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('DDP001', 'false', 10);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('DDP002', 'false', 10);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('DDP003', 'false', 10);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('DDP004', 'false', 10);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MI0001', 'false', 11);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MI0002', 'false', 11);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MI0003', 'false', 11);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MI0004', 'false', 11);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AIS001', 'false', 12);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AIS002', 'false', 12);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AIS003', 'false', 12);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AIS004', 'false', 12);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AIS005', 'false', 12);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('IEXP01', 'false', 13);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('IEXP02', 'false', 13);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('IEXP03', 'false', 13);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('IEXP04', 'false', 13);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLA006', 'false', 14);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLA006', 'false', 14);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLA006', 'false', 14);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLA006', 'false', 14);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLA006', 'false', 14);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLA006', 'false', 14);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PG0001', 'false', 15);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PG0002', 'false', 15);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PG0003', 'false', 15);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PG0004', 'false', 15);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PG0005', 'false', 15);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PG0006', 'false', 15);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PG0007', 'false', 15);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('JIS001', 'false', 16);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('JIS002', 'false', 16);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('JIS003', 'false', 16);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0001', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0002', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0003', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0004', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0005', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0006', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0007', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0008', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0009', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CMU0010', 'false', 17);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('NOTB001', 'false', 20);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('NOTB002', 'false', 20);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('NOTB003', 'false', 20);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOL0001', 'false', 21);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOL0002', 'false', 21);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOL0003', 'false', 21);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOL0004', 'false', 21);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOL0005', 'false', 21);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOL0006', 'false', 21);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLOG01', 'false', 22);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLOG02', 'false', 22);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLOG03', 'false', 22);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLOG04', 'false', 22);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLOG05', 'false', 22);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLOG06', 'false', 22);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('TECLOG07', 'false', 22);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOAC01', 'false', 23);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOAC02', 'false', 23);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOAC03', 'false', 23);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('MOAC04', 'false', 23);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CPU01', 'false', 24);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CPU02', 'false', 24);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CPU03', 'false', 24);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('CPU04', 'false', 24);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AS001', 'false', 25);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AS002', 'false', 25);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AS003', 'false', 25);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AS004', 'false', 25);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AS005', 'false', 25);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AS006', 'false', 25);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('AS007', 'false', 25);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PHP001', 'false', 26);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PHP002', 'false', 26);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PHP003', 'false', 26);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('PHP004', 'false', 26);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('WCPH01', 'false', 27);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('WCPH02', 'false', 27);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('WCPH03', 'false', 27);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('WCPH04', 'false', 27);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('JOLO001', 'false', 28);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('JOLO002', 'false', 28);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('JOLO003', 'false', 28);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM8001', 'false', 29);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM8002', 'false', 29);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM8003', 'false', 29);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM8004', 'false', 29);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM8005', 'false', 29);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM8006', 'false', 29);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM4001', 'false', 30);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM4002', 'false', 30);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM4003', 'false', 30);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM4004', 'false', 30);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM2001', 'false', 31);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM2002', 'false', 31);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM2003', 'false', 31);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM2004', 'false', 31);
--INSERT INTO "ejemplar"("numeroSerie", "vendido", "producto")
--values ('RAM2005', 'false', 31);


CREATE TABLE "combo" (
	"id" serial NOT NULL,
	"nombre" character varying (50),
	"total" float,
	"descuento" float,
	"totalConDescuento" float,
	"vendido" boolean,
	Primary key ("id")
);

--- CARGA DE COMBOS
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('Computadora completa', 1700, 10, 11970, 'False');
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('Combo notebook', 45800, 20, 36640, 'False');
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('Combo accesorios', 7270, 15, 6179.5, 'False');
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('Combo Logitech', 8100, 20, 6480, 'False');
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('Combo Philips', 13300, 30, 9310, 'False');
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('PC completa', 69200, 25, 51900, 'False');
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('Combo gamer', 9590, 20, 7672, 'False');
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('Accesorios computadora', 8025, 15, 6821.25, 'False');
--INSERT INTO "combo"("nombre", "total", "descuento", "totalConDescuento", "vendido")
--values ('Combo pc', 62455, 25, 46841.25, 'False');

CREATE TABLE "ejemplar_combo" (
	"idCombo" smallint NOT NULL,
	"numeroSerie" character varying(50) NOT NULL,
	foreign key ("idCombo") references "combo" deferrable,
	foreign key ("numeroSerie") references "ejemplar" deferrable
);

--- CARGA DE EJEMPLARES AL COMBO
--- ATENCION CAMBIAR LOS ID DEL COMBO
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (33, '12345');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (33, '6789');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (34, 'JIS001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (34, 'AIS001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (34, 'PHP001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (37, 'MI0002');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (37, 'AIS002');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (37, 'TECLA001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (37, 'PG0001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (38, 'CPU01');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (38, 'MLP01');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (38, 'TECLA001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (38, 'MOL0001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (33, 'RAM8001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (44, 'NOTB001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (44, 'AS001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (45, 'CPU01');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (45, 'MOAC01');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (45, 'TECLOG01');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (45, 'MOL0001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (46, 'MI0002');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (46, 'AIS002');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (46, 'PG0001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (47, 'MOL0002');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (47, 'TECLOG02');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (47, 'JOLO001');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (48, 'MLP01');
--INSERT INTO "ejemplar_combo"("idCombo", "numeroSerie") values (48, 'WCPH01');


CREATE TABLE "carrito" (
	"id" serial NOT NULL,
	"total" float,
	"usuario" character varying(150),
	"finalizado" boolean,
	Primary key ("id")
);

CREATE TABLE "ejemplar_carrito" (
	"idCarrito" integer NOT NULL,
	"numeroSerie" character varying(50) NOT NULL,
	foreign key ("idCarrito") references "carrito" deferrable,
	foreign key ("numeroSerie") references "ejemplar" deferrable
);

CREATE TABLE "combo_carrito" (
	"idCarrito" integer NOT NULL,
	"idCombo" integer NOT NULL,
	foreign key ("idCarrito") references "carrito" deferrable,
	foreign key ("idCombo") references "combo" deferrable
);

CREATE TABLE "compra" (
	"id" serial NOT NULL,
	"idCarrito" integer NOT NULL,
	"montoCompra" float NOT NULL, 
	"estadoConfirmacion" boolean,
	Primary key ("id"),
	foreign key ("idCarrito") references "carrito" deferrable
);

CREATE TABLE "pago" (
	"id" serial NOT NULL,
	"idCompra" integer NOT NULL,
	"total" double precision NOT NULL,
	"estado" boolean,
	"tarjeta" character varying (50),
	"cuotas" integer,
	Primary key ("id"),
	foreign key ("idCompra") references "compra" deferrable
);

CREATE TABLE "mercadopago" (
	"id" character varying (200),
	"idCompra" integer NOT NULL,
	"total" double precision NOT NULL,
	"link_pago" character varying (1000),
	"estado" boolean,
	Primary key ("id"),
	foreign key ("idCompra") references "compra" deferrable
);

--Setear datos por defecto 
INSERT INTO "rol" ("nombreRol") values ('admin');


---TRIGGERS
---La contraseña de usuario no puede tener menos de 5 caracteres de longitud ni más de 20.
CREATE OR REPLACE FUNCTION nuevaContrasenia()
RETURNS trigger AS $verificarContrasenia$
BEGIN
IF (char_length(NEW.contrasenia)<5) THEN
RAISE EXCEPTION 'La contraseña es muy corta, debe superar los 5 caracteres ';
rollback transaction;
ELSE
IF (20 < char_length(NEW.contrasenia)) THEN
RAISE EXCEPTION 'La contraseña es muy larga, no debe superar los 20 caracteres ';
rollback transaction;
ELSE 
RETURN NEW;
END IF;
END IF; 
END;
$verificarContrasenia$ 
LANGUAGE plpgsql;

CREATE TRIGGER verificarContrasenia
BEFORE INSERT ON "usuario"
FOR EACH ROW
EXECUTE PROCEDURE nuevaContrasenia();


---Actualizar La contraseña de usuario no puede tener menos de 5 caracteres de longitud ni más de 20.
CREATE OR REPLACE FUNCTION actualizarContrasenia()
RETURNS trigger AS $verificarActualizarContrasenia$
BEGIN
IF (char_length(NEW.contrasenia)<5) THEN
RAISE EXCEPTION 'La contraseña es muy corta, debe superar los 5 caracteres ';
rollback transaction;
ELSE
IF (20 < char_length(NEW.contrasenia)) THEN
RAISE EXCEPTION 'La contraseña es muy larga, no debe superar los 20 caracteres ';
rollback transaction;
ELSE 
RETURN NEW;
END IF;
END IF; 
END;
$verificarActualizarContrasenia$ 
LANGUAGE plpgsql;

CREATE TRIGGER verificarActualizarContrasenia
BEFORE UPDATE ON "usuario"
FOR EACH ROW
EXECUTE PROCEDURE actualizarContrasenia();




--- El precio del producto no puede ser menor o igual a cero
CREATE OR REPLACE FUNCTION cargandoPrecio()
RETURNS trigger AS
$cargarPrecio$
BEGIN
IF (NEW.precio <=0) THEN
RAISE EXCEPTION 'Precio no válido ';
rollback transaction;
ELSE
RETURN NEW;
END IF;
END;
$cargarPrecio$
LANGUAGE plpgsql;

CREATE TRIGGER cargarPrecio
BEFORE INSERT ON "producto"
FOR EACH ROW
EXECUTE PROCEDURE cargandoPrecio();


--Test Trigger Precio menor o igual a 0 
/*
INSERT INTO "tipoProducto"("nombreTipo") values ('mouse');
INSERT INTO "marca"("nombre") values ('Logitrch');

INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
values ('mause 1 ', 'descripcion 1 ', -10, 'm320', 12, 1, 1);
*/



--- El total del combo no puede ser menor o igual a cero
/*
CREATE OR REPLACE FUNCTION cargandoTotal()
RETURNS trigger AS
$cargarTotal$
BEGIN
IF (NEW.total <=0) THEN
RAISE EXCEPTION 'Total no válido ';
rollback transaction;
ELSE
RETURN NEW;
END IF;
END;
$cargarTotal$
LANGUAGE plpgsql;

CREATE TRIGGER cargarTotal
BEFORE INSERT ON "combo"
FOR EACH ROW
EXECUTE PROCEDURE cargandoTotal();
*/

--Test Total sobre Cobo
--INSERT INTO "combo" ("nombre", "total", "descuento") VALUES ('combo 1', -12, 1.0);


-- Control de unico usuario nuevo 
CREATE OR REPLACE FUNCTION verificandoUnicoUsuario()
RETURNS trigger AS $verificarUnicoUsuario$
DECLARE r integer;
BEGIN
r := (SELECT COUNT(*) FROM usuario WHERE "nombre" = NEW."nombre");
IF (r > 0) THEN
RAISE EXCEPTION 'El usario ya existe';
rollback transaction;
ELSE 
RETURN NEW;
END IF;
END;
$verificarUnicoUsuario$ 
LANGUAGE plpgsql;

CREATE TRIGGER verificarUnicoUsuario
BEFORE INSERT ON "usuario"
FOR EACH ROW
EXECUTE PROCEDURE verificandoUnicoUsuario();

--TEST Trigger 
--INSERT INTO "usuario" ("nombre", "contrasenia", "contacto", "rol" ) values ('Mario@aaa', '123123', 'etrada 10030', 1); 

-------
-- Control de unico rol nuevo 
CREATE OR REPLACE FUNCTION verificandoUnicoRol()
RETURNS trigger AS $verificarUnicoRol$
DECLARE r integer;
BEGIN
r := (SELECT COUNT(*) FROM rol WHERE "nombreRol" = NEW."nombreRol");
IF (r > 0) THEN
RAISE EXCEPTION 'El Rol ya existe';
rollback transaction;
ELSE 
RETURN NEW;
END IF;
END;
$verificarUnicoRol$ 
LANGUAGE plpgsql;

CREATE TRIGGER verificarUnicoRol
BEFORE INSERT ON "rol"
FOR EACH ROW
EXECUTE PROCEDURE verificandoUnicoRol();

--Test Trigger
--INSERT INTO "rol" ("nombreRol") values ('admin');


---------------
-------
-- Control de unica Marca nuevo 
CREATE OR REPLACE FUNCTION verificandoUnicoMarca()
RETURNS trigger AS $verificarUnicoMarca$
DECLARE r integer;
BEGIN
r := (SELECT COUNT(*) FROM marca WHERE "nombre" = NEW."nombre");
IF (r > 0) THEN
RAISE EXCEPTION 'La Marca ya existe';
rollback transaction;
ELSE 
RETURN NEW;
END IF;
END;
$verificarUnicoMarca$ 
LANGUAGE plpgsql;

CREATE TRIGGER verificarUnicoMarca
BEFORE INSERT ON "marca"
FOR EACH ROW
EXECUTE PROCEDURE verificandoUnicoMarca();

--Test Trigger
--INSERT INTO "marca"("nombre") values ('Logitrch');


--------------------------
-- Control de unico Producto nuevo 
CREATE OR REPLACE FUNCTION verificandoUnicoProducto()
RETURNS trigger AS $verificarUnicoProducto$
DECLARE r integer;
BEGIN
r := (SELECT COUNT(*) FROM producto WHERE "nombre" = NEW."nombre");
IF (r > 0) THEN
RAISE EXCEPTION 'El Producto ya existe';
rollback transaction;
ELSE 
RETURN NEW;
END IF;
END;
$verificarUnicoProducto$ 
LANGUAGE plpgsql;

CREATE TRIGGER verificarUnicoProducto
BEFORE INSERT ON "producto"
FOR EACH ROW
EXECUTE PROCEDURE verificandoUnicoProducto();

--Test Tigger 
/*
INSERT INTO "producto"("nombre", "descripcion", "precio", "modelo","garantia", "tipoProducto","marca" )
values ('mause 1 ', 'descripcion 1 ', 10, 'm320', 12, 1, 1);
*/


--------------------------
-- Control de unico Tipo de Producto nuevo 
CREATE OR REPLACE FUNCTION verificandoUnicoTipoProducto()
RETURNS trigger AS $verificarUnicoTipoProducto$
DECLARE r integer;
BEGIN
r := (SELECT COUNT(*) FROM "tipoProducto" WHERE "nombreTipo" = NEW."nombreTipo");
IF (r > 0) THEN
RAISE EXCEPTION 'El Tipo de Producto ya existe';
rollback transaction;
ELSE 
RETURN NEW;
END IF;
END;
$verificarUnicoTipoProducto$ 
LANGUAGE plpgsql;

CREATE TRIGGER verificarUnicoTipoProducto
BEFORE INSERT ON "tipoProducto"
FOR EACH ROW
EXECUTE PROCEDURE verificandoUnicoTipoProducto();


--Test Tigger 

--INSERT INTO "tipoProducto"("nombreTipo") values ('mouse');


--------------------------------
-- Vistas DB
--------------------------------

--VISTA detalle de Ejemplares
CREATE OR REPLACE VIEW vista_ejemplares AS
SELECT 
	e."numeroSerie", 
	e."vendido", 
	p."nombre", 
	p."descripcion",
	p."precio",
	p."modelo",
	"m"."nombre" AS "marca",
	tp."nombreTipo" AS "tipoProducto"
FROM ejemplar AS e
JOIN producto AS "p" ON e."producto" = p."id"  
JOIN marca AS "m" ON m."idMarca" = p."marca"
JOIN "tipoProducto" AS "tp" ON tp."idTipo" = p."tipoProducto";

----
----Vista Productos
CREATE OR REPLACE VIEW vista_productos AS
SELECT
	p."id",
 	p."nombre", 
	p."descripcion",
	p."precio",
	p."modelo",
	p."garantia",
	"m"."nombre" AS "marca",
	tp."nombreTipo" AS "tipoProducto"
FROM producto AS p 
JOIN marca AS "m" ON m."idMarca" = p."marca"
JOIN "tipoProducto" AS "tp" ON tp."idTipo" = p."tipoProducto";

-----

----- Vista Usuarios 
CREATE OR REPLACE VIEW vista_usuarios AS
SELECT 
	u."nombre",
	u."contrasenia", 
	u."contacto", 
	r."nombreRol" 
FROM usuario AS u
JOIN rol AS r ON r."idRol" = u."rol" ;   

--------
---Vista Ejemplar_combo
CREATE OR REPLACE VIEW vista_ejemplar_combo AS
SELECT
ec."idCombo",
ec."numeroSerie",
e."vendido",
e."producto",
p."nombre",
p."precio",
c."id",
c."total",
c."descuento",
c."totalConDescuento"
FROM ejemplar_combo AS ec
JOIN ejemplar AS "e" ON ec."numeroSerie" = e."numeroSerie"
JOIN combo AS "c" ON ec."idCombo" = c."id"
Join producto AS "p" ON e.producto = p."id";


---VISTA EJEMPLAR CARRITO
CREATE OR REPLACE VIEW vista_ejemplar_carrito AS
SELECT
ec."idCarrito",
ec."numeroSerie",
e."vendido",
e."producto",
p."nombre",
c."id",
c."usuario",
c."finalizado",
c."total",
p."precio"
FROM ejemplar_carrito AS ec
JOIN ejemplar AS "e" ON ec."numeroSerie" = e."numeroSerie"
JOIN carrito AS "c" ON ec."idCarrito" = c."id"
Join producto AS "p" ON e.producto = p."id";


---VISTA COMBO CARRITO
CREATE OR REPLACE VIEW vista_combo_carrito AS
SELECT
cc."idCarrito",
cc."idCombo",
co."nombre",
co."totalConDescuento"
FROM combo_carrito AS cc
JOIN combo AS "co" ON cc."idCombo" = co."id"
JOIN carrito AS "c" ON cc."idCarrito" = c."id";


--------
---Vista Ejemplar_combo
CREATE OR REPLACE VIEW vista_compras AS
SELECT
co."id",
co."idCarrito",
co."montoCompra",
co."estadoConfirmacion",
ca."usuario"
FROM compra AS co
JOIN carrito AS "ca" ON ca."id" = co."idCarrito";


---VISTA EJEMPLAR COMPRA
CREATE OR REPLACE VIEW vista_ejemplar_compra AS
SELECT
ec."idCarrito",
ec."numeroSerie",
co."id"
FROM ejemplar_carrito AS ec
JOIN carrito AS "c" ON ec."idCarrito" = c."id"
Join compra AS "co" ON co."idCarrito" = c."id";

--INSERTs de inicio 
-- admin por defecto
INSERT INTO public.usuario(
	nombre, contrasenia, contacto, rol)
	VALUES ('admin@admin.com', '123456', '', 1);

--- AGREGA EL CAMPO USUARIO A LA TABLA CARRITO
--- ALTER TABLE "carrito" ADD COLUMN "usuario" character varying(150);

--- AGREGA EL CAMPO FINALIZADO A LA TABLA CARRITO
--- ALTER TABLE "carrito" ADD COLUMN "finalizado" boolean;

--- AGREGA EL CAMPO VENDIDO A LA TABLA COMBO
--- ALTER TABLE "combo" ADD COLUMN "vendido" boolean;