// Initialize scene, camera, and renderer
let scene = new THREE.Scene();
let camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
let renderer = new THREE.WebGLRenderer({ canvas: document.querySelector('#threeCanvas') });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create a Riemann Zeta Function curve path
function createZetaCurve() {
    let curve = new THREE.CatmullRomCurve3([
        new THREE.Vector3(-10, 0, 0),
        new THREE.Vector3(-5, 5, 0),
        new THREE.Vector3(0, 0, 0),
        new THREE.Vector3(5, -5, 0),
        new THREE.Vector3(10, 0, 0)
    ]);
    let points = curve.getPoints(50);
    let geometry = new THREE.BufferGeometry().setFromPoints(points);
    let material = new THREE.LineBasicMaterial({ color: 0xff0000 });
    let curveObject = new THREE.Line(geometry, material);
    scene.add(curveObject);
    return curve;
}

// Create planets/stars in the solar system
function createPlanet(x, y, z, name) {
    let geometry = new THREE.SphereGeometry(1, 32, 32);
    let material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    let planet = new THREE.Mesh(geometry, material);
    planet.position.set(x, y, z);
    planet.name = name; // Name each planet for interactions
    scene.add(planet);
    return planet;
}

// Add interactive planets to the scene
let planet1 = createPlanet(0, 0, -10, 'Riemann Hypothesis');
let planet2 = createPlanet(-20, 10, -30, 'P vs NP');
let planet3 = createPlanet(20, -15, 10, 'Navier-Stokes');

// Add lighting
let light = new THREE.PointLight(0xffffff, 1, 100);
light.position.set(50, 50, 50);
scene.add(light);

// Create and render the Riemann Zeta Function curve
let zetaCurve = createZetaCurve();

// Position the camera
camera.position.z = 30;

// Handle interactivity (click events)
function onDocumentMouseDown(event) {
    event.preventDefault();
    
    let mouse = new THREE.Vector2();
    let raycaster = new THREE.Raycaster();
    
    // Calculate mouse position in normalized device coordinates (-1 to +1)
    mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    
    raycaster.setFromCamera(mouse, camera);
    
    // Check which objects are intersected
    let intersects = raycaster.intersectObjects([planet1, planet2, planet3]);
    if (intersects.length > 0) {
        let planetName = intersects[0].object.name;
        alert(`Welcome to ${planetName}! Here you'll explore ${planetName} and dive into one of the unsolved problems of mathematics!`);
    }
}

// Add event listener for mouse clicks
document.addEventListener('mousedown', onDocumentMouseDown, false);

// Smooth camera movement along the zeta curve
function smoothCameraMovement(curve) {
    let t = 0;
    function animate() {
        t += 0.001;  // Increment t for smooth movement
        if (t > 1) t = 0;  // Loop back to the start

        let point = curve.getPointAt(t);  // Get the point on the curve at parameter t
        camera.position.set(point.x, point.y, point.z + 10);  // Position camera slightly above the curve

        renderer.render(scene, camera);
        requestAnimationFrame(animate);
    }
    animate();
}

// Call the smooth camera movement function
smoothCameraMovement(zetaCurve);

// Function to scale the zeta curve dynamically
function updateCurveScale(scale) {
    zetaCurve.scale.set(scale, scale, scale);  // Adjust the scale of the Riemann Zeta curve
    renderer.render(scene, camera);
}

// Handle space travel (keyboard controls)
function handleSpaceTravel() {
    document.addEventListener('keydown', function(event) {
        switch(event.code) {
            case 'ArrowUp':
                camera.position.y += 1;  // Move the camera upward
                break;
            case 'ArrowDown':
                camera.position.y -= 1;  // Move the camera downward
                break;
            case 'ArrowLeft':
                camera.position.x -= 1;  // Move the camera left
                break;
            case 'ArrowRight':
                camera.position.x += 1;  // Move the camera right
                break;
        }
        renderer.render(scene, camera);
    });
}

// Activate space travel
handleSpaceTravel();
