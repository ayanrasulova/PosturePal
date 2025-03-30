document.addEventListener("DOMContentLoaded", function () {
    let frameIndex = 0;
    let interval;
    const img = document.getElementById("giraffeAnimation");

    const animations = {
        bad: { frames: ["/static/posturepal/assets/bad1.png", "/static/posturepal/assets/bad2.png"], fps: 3 },
        ok: { frames: ["/static/posturepal/assets/ok1.png", "/static/posturepal/assets/ok2.png"], fps: 3 },
        good: { frames: ["/static/posturepal/assets/good1.png", "/static/posturepal/assets/good2.png", "/static/posturepal/assets/good3.png"], fps: 7 }
    };

    function startAnimation(state) {
        clearInterval(interval); // Stop any existing animation

        if (!animations[state]) return;

        const { frames, fps } = animations[state];
        frameIndex = 0;

        if (state === "good") {
            // Show chomp first when "good" is flagged, at 7fps
            img.src = "/static/posturepal/assets/chomp.png";
            setTimeout(() => {
                // Start looping good frames after the chomp frame for 1/7th of a second (7fps)
                frameIndex = 0;
                img.src = frames[frameIndex];

                interval = setInterval(() => {
                    frameIndex = (frameIndex + 1) % frames.length;
                    img.src = frames[frameIndex];
                }, 1000 / fps);
            }, 1000 / 7); // 1 frame at 7 FPS (1/7 seconds)
        } else {
            // Start bad or ok animation directly
            img.src = frames[frameIndex];
            interval = setInterval(() => {
                frameIndex = (frameIndex + 1) % frames.length;
                img.src = frames[frameIndex];
            }, 1000 / fps);
        }
    }

    // Example: Simulate condition changes
    setTimeout(() => startAnimation('bad'), 1000);  // Start with "bad"
    setTimeout(() => startAnimation('ok'), 5000);   // Switch to "ok"
    setTimeout(() => startAnimation('good'), 10000); // Switch to "good"
});
