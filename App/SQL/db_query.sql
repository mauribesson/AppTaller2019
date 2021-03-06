
CREATE TABLE "rol" (
	"idRol" serial NOT NULL,
	"nombreRol" character varying (30) NOT NULL,
	Primary Key ("idRol")
);
--ROLES
--ADMIN ID 1
--COMPRADOR ID 2
--VENDEDOR ID 3

---CARGA DE ROLES
INSERT INTO "rol" ("nombreRol") values ('admin');
INSERT INTO "rol" ("nombreRol") values ('comprador');
INSERT INTO "rol" ("nombreRol") values ('vendedor');

CREATE TABLE "usuario" (
	"nombre" character varying(150) NOT NULL,
	"contrasenia" character varying (20) NOT NULL, 
	"contacto" character varying (70),
	"rol" smallint NOT NULL,
	Primary Key ("nombre"),
	foreign key ("rol") references "rol" deferrable
);



CREATE TABLE "tipoProducto" (
	"idTipo" serial NOT NULL,
	"nombreTipo" character varying(30) NOT NULL,
	Primary key ("idTipo")
);


CREATE TABLE "marca" (
	"idMarca" serial NOT NULL,
	"nombre" character varying(30) NOT NULL,
	Primary key ("idMarca")
);


CREATE TABLE "producto" (
	"id" serial NOT NULL,
	"nombre" character varying (30) NOT NULL,
	"descripcion" character varying (1000) NOT NULL,
	"precio" float NOT NULL,
	"modelo" character varying (30),
	"garantia" smallint,
	"tipoProducto" smallint,
	"marca" smallint,
	Primary key ("id"),
	foreign key ("tipoProducto") references "tipoProducto" deferrable,
	foreign key ("marca") references "marca" deferrable
);


CREATE TABLE "imagenes" (
	"id" serial NOT NULL,
	"idProducto" smallint NOT NULL,
	"urlImagen" character varying (500) NOT NULL,
	Primary key ("id"),
	foreign key ("idProducto") references "producto" deferrable
);


CREATE TABLE "ejemplar" (
	"numeroSerie" character varying(50) NOT NULL,
	"vendido" boolean NOT NULL,
	"producto" smallint NOT NULL,
	Primary key ("numeroSerie"),
	foreign key ("producto") references "producto" deferrable
);


CREATE TABLE "combo" (
	"id" serial NOT NULL,
	"nombre" character varying (50),
	"total" float,
	"descuento" float,
	"totalConDescuento" float,
	"vendido" boolean,
	Primary key ("id")
);


CREATE TABLE "ejemplar_combo" (
	"idCombo" smallint NOT NULL,
	"numeroSerie" character varying(50) NOT NULL,
	foreign key ("idCombo") references "combo" deferrable,
	foreign key ("numeroSerie") references "ejemplar" deferrable
);



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
	"fecha" date,
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
RAISE EXCEPTION 'La contraseña es muy corta, debe ser igual o superar los 5 caracteres ';
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
---Vista compras
CREATE OR REPLACE VIEW vista_compras AS
SELECT
co."id",
co."idCarrito",
co."montoCompra",
co."fecha",
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


--------
CREATE OR REPLACE VIEW compra_pago AS
SELECT
co."id",
co."idCarrito",
co."montoCompra",
co."fecha",
co."estadoConfirmacion",
pa."idCompra",
pa."estado",
ca."usuario"
FROM compra AS co
JOIN carrito AS "ca" ON ca."id" = co."idCarrito"
JOIN mercadopago AS "pa" ON pa."idCompra" = co."id";

-- ====================================fin vistas
