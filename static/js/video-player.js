var videoVolumeControl = document.getElementById("video-vol-control");
var video = document.getElementById("video");
var videoPlayPause = document.getElementById("video-play-pause");
var videoProgress = document.getElementById("video-progress");

let videoPlaying = false;

// Video Play and Pause
console.log(video.duration);
videoPlayPause.addEventListener("click", togglePlayPause);

document.getElementById("video").addEventListener("click", togglePlayPause);

 // Video Volume Controls

videoVolumeControl.addEventListener("change", function () {
  video.volume = this.value / 100;
});

videoVolumeControl.addEventListener("input", function () {
  video.volume = this.value / 100;
});

// Video Slider Controls

videoProgress.addEventListener("change", function () {  
  var newTime = (this.value / 100) * video.duration;
  video.currentTime = newTime;
});

// Video Slider 

video.addEventListener("timeupdate", function () {  
  var sliderPosition = video.currentTime / video.duration;
  videoProgress.style.width = sliderPosition * 100 + "%"

  if (video.ended) {
    videoPlaying = false;
    videoPlayPause.setAttribute("name", "reload-circle");
  }
});

function togglePlayPause() {
  if (videoPlaying) {
    videoPlaying = false;
    video.pause();
    videoPlayPause.setAttribute("name", "play");
  } else {
    videoPlaying = true;
    video.play();
    videoPlayPause.setAttribute("name", "pause");
  }
}