// 2. **Verificador de par/impar**
// - Genera un número y determina si es par o impar.

// Genera un número aleatorio entre 1 y 100
const numero = Math.floor(Math.random() * 100) + 1;

console.log(`Número generado: ${numero}`);

if (numero % 2 === 0) {
  console.log(`${numero} es par.`);
  process.exit(0); // Salida exitosa
} else {
  console.log(`${numero} es impar.`);
  process.exit(0); // Salida exitosa
}