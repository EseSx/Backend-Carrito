// =============================
//          IMPORTANTE
// =============================
// Voy a intentar explicar lo mas rapido y facil que pueda
// Primero voy a crear los forms que vos vas a poder usar en react
// Despues como se deben pasar esos datos, incluyendo normalizacion y todo
// Y por ultimo el fetch
// Si copias y pegas deberia andar

// =============================
//             AUTOS
// =============================

// ---- Ingresar ----
// <form id="formularioIngresarAutos">
//   <input type="text" name="modelo" />
//   <input type="number" name="disponibles" min="0" />
//   <input type="number" step="any" name="precio_por_dia" min="0" />
//   <button type="submit">Enviar</button>
// </form>

// const formularioIngresarAutos = document.getElementById(
//   "formularioIngresarAutos"
// );

// formularioIngresarAutos.addEventListener("submit", (event) => {
//   event.preventDefault();

//   const formData = new FormData(formularioIngresarAutos);

//   let data = Object.fromEntries(formData);
//   // El contenido de data va a ser un diccionario, formado por los name de cada input como claves, y con los propios valores que se les hayan ingresado
//   // Este data se veria asi:
//   // {modelo: ..., disponibles: ..., precio_por_dia: ...}

//   // Para terminar de normalizar convertimos los valores al formato requerido
//   data.disponibles = parseInt(data.disponibles);
//   data.precio_por_dia = parseFloat(data.precio_por_dia);

// fetch("https://backend-carrito-filb.vercel.app/autos/ingresar", {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//   },
//   body: JSON.stringify(data),
// })
//   .then(async (res) => {
//     if (!res.ok) {
//       const errorText = await res.text();
//       throw new Error(`Server error: ${res.status} ${errorText}`);
//     }
//     return res.json();
//   })
//   .then((res) => console.log(res))
//   .catch(console.error);

// =============================
//           CLIENTES
// =============================
// ---- Ingresar ----
// <form id="formularioIngresarCliente">
//   <input type="text" name="nombre" />
//   <input type="text" name="apellido" />
//   <input type="password" name="contraseña" />
//   <input type="email" name="correo_electronico" />
//   <button type="submit">Enviar</button>
// </form>

// const formularioIngresarCliente = document.getElementById(
//   "formularioIngresarCliente"
// );

// formularioIngresarCliente.addEventListener("submit", (event) => {
//   event.preventDefault();

//   const formData = new FormData(formularioIngresarCliente);

//   let data = Object.fromEntries(formData);

// fetch("https://backend-carrito-filb.vercel.app/clientes/ingresar", {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//   },
//   body: JSON.stringify(data),
// })
//   .then(async (res) => {
//     if (!res.ok) {
//       const errorText = await res.text();
//       throw new Error(`Server error: ${res.status} ${errorText}`);
//     }
//     return res.json();
//   })
//   .then((res) => console.log(res))
//   .catch(console.error);

let data = {
  modelo: "Falcon",
  disponible: 50,
  precio_por_dia: 2000.75,
};

fetch("https://backend-carrito-filb.vercel.app/autos/ingresar", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
})
  .then(async (res) => {
    if (!res.ok) {
      const errorText = await res.text();
      throw new Error(`Server error: ${res.status} ${errorText}`);
    }
    return res.json();
  })
  .then((res) => console.log(res))
  .catch(console.error);
