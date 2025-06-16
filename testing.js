data = {
  usuarioIngresado: "administracionViajes@gmail.com",
  contraseñaIngresada: "contraseñaDeLaAdministracion",
};

fetch(
  "https://backend-carrito-alpha.vercel.app/clientes/validarContrasenaAdmin",
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  }
)
  .then((res) => res.json())
  .then((res) => console.log(res));
