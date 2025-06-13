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

//   const data = Object.fromEntries(formData);
//   // El contenido de data va a ser un diccionario, formado por los name de cada input como claves, y con los propios valores que se les hayan ingresado
//   // Este data se veria asi:
//   // {modelo: ..., disponibles: ..., precio_por_dia: ...}

//   fetch("https://backend-carrito-filb.vercel.app/autos/ingresar", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(data),
//   })
//     .then((res) => res.json())
//     .then((res) => console.log(res));
// });

fetch("https://backend-carrito-filb.vercel.app/autos/ingresar", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    modelo: "auto",
    disponibles: "2",
    precio_por_dia: "250,00",
  }),
})
  .then((res) => res.json())
  .then((res) => console.log(res))
  .catch(Error);
