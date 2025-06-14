// =============================
//            IGNORAR
// =============================
// ---- Codigo de react ----
//   import React, { useState } from "react";

// function FormularioIngresarCliente() {
//   const [formData, setFormData] = useState({
//     nombre: "",
//     apellido: "",
//     contraseña: "",
//     correo_electronico: "",
//   });

//   const handleChange = (e) => {
//     const { name, value } = e.target;
//     setFormData((prev) => ({
//       ...prev,
//       [name]: value,
//     }));
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     try {
//       const res = await fetch(
//         "https://backend-carrito-filb.vercel.app/clientes/ingresar",
//         {
//           method: "POST",
//           headers: {
//             "Content-Type": "application/json",
//           },
//           body: JSON.stringify(formData),
//         }
//       );

//       if (!res.ok) {
//         const errorText = await res.text();
//         throw new Error(`Server error: ${res.status} ${errorText}`);
//       }

//       const result = await res.json();
//       console.log(result);
//     } catch (error) {
//       console.error(error);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <input
//         type="text"
//         name="nombre"
//         value={formData.nombre}
//         onChange={handleChange}
//         placeholder="Nombre"
//       />
//       <input
//         type="text"
//         name="apellido"
//         value={formData.apellido}
//         onChange={handleChange}
//         placeholder="Apellido"
//       />
//       <input
//         type="password"
//         name="contraseña"
//         value={formData.contraseña}
//         onChange={handleChange}
//         placeholder="Contraseña"
//       />
//       <input
//         type="email"
//         name="correo_electronico"
//         value={formData.correo_electronico}
//         onChange={handleChange}
//         placeholder="Correo Electrónico"
//       />
//       <button type="submit">Enviar</button>
//     </form>
//   );
// }

// export default FormularioIngresarCliente;

let data = {
  uc_id: 8,
};

fetch("http://0.0.0.0:8000/clientes/obtenerId", {
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

// fetch("http://0.0.0.0:8000/clientes/obtener")
//   .then((res) => res.json())
//   .then((res) => console.log(res));
