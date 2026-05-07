const canvas = document.getElementById("sphere");
const ctx = canvas.getContext("2d");

canvas.width = 400;
canvas.height = 400;

let particles = [];
const radius = 150;
const total = 800;

// create sphere points
for (let i = 0; i < total; i++) {
  const phi = Math.acos(1 - 2 * Math.random());
  const theta = 2 * Math.PI * Math.random();

  const x = radius * Math.sin(phi) * Math.cos(theta);
  const y = radius * Math.sin(phi) * Math.sin(theta);
  const z = radius * Math.cos(phi);

  particles.push({ x, y, z });
}

let angle = 0;

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  angle += 0.01;

  particles.forEach(p => {
    // rotate around Y axis
    let x = p.x * Math.cos(angle) - p.z * Math.sin(angle);
    let z = p.x * Math.sin(angle) + p.z * Math.cos(angle);

    let y = p.y;

    // perspective
    const scale = 300 / (300 + z);
    const px = x * scale + canvas.width / 2;
    const py = y * scale + canvas.height / 2;

    // glow effect
    ctx.fillStyle = "cyan";
    ctx.globalAlpha = scale;

    ctx.beginPath();
    ctx.arc(px, py, 1.5, 0, Math.PI * 2);
    ctx.fill();
  });

  requestAnimationFrame(animate);
}

animate();