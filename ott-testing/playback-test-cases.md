# OTT Playback Test Cases

This document contains sample test cases for validating video playback functionality in an OTT platform.

---

## TC_PLAYBACK_001 — Start Video Playback

**Test Type:** Functional Testing  
**Priority:** High

### Preconditions
- User is logged in.
- Valid playable content is available.
- Device has a stable network connection.

### Test Steps
1. Launch the OTT application.
2. Navigate to a playable movie, episode, or live channel.
3. Select the content.
4. Start playback.

### Expected Result
The selected content should start playing successfully without errors or buffering.

---

## TC_PLAYBACK_002 — Play/Pause Functionality

**Test Type:** Functional Testing  
**Priority:** High

### Test Steps
1. Start video playback.
2. Select the Pause option.
3. Observe the video.
4. Select Play.

### Expected Result
- Video should pause when Pause is selected.
- Video should resume when Play is selected.

---

## TC_PLAYBACK_003 — Seek Functionality

**Test Type:** Functional Testing  
**Priority:** High

### Test Steps
1. Start video playback.
2. Move the playback seek bar forward.
3. Observe the playback position.
4. Move the seek bar backward.

### Expected Result
The video should move to the selected playback position and continue playing correctly.

---

## TC_PLAYBACK_004 — Audio and Video Synchronization

**Test Type:** Playback Testing  
**Priority:** High

### Test Steps
1. Start video playback.
2. Observe the audio and corresponding video actions.
3. Monitor playback for synchronization issues.

### Expected Result
Audio should remain synchronized with the corresponding video throughout playback.

---

## TC_PLAYBACK_005 — Playback Under Poor Network Conditions

**Test Type:** Network / Playback Testing  
**Priority:** High

### Test Steps
1. Start video playback under a stable network.
2. Introduce reduced network bandwidth.
3. Continue monitoring playback.
4. Observe buffering and recovery behaviour.

### Expected Result
The application should handle network degradation gracefully and recover playback when network conditions improve.

---

## TC_PLAYBACK_006 — Skip Intro Marker

**Test Type:** Functional Testing  
**Priority:** Medium

### Test Steps
1. Start playback of content containing a Skip Intro marker.
2. Wait until the Skip Intro option appears.
3. Select Skip Intro.

### Expected Result
Playback should skip the intro section and continue from the expected timestamp.

---

## TC_PLAYBACK_007 — Recap Marker

**Test Type:** Functional Testing  
**Priority:** Medium

### Test Steps
1. Start an episode containing a Recap marker.
2. Verify the Recap option is displayed at the appropriate point.
3. Select the Recap option.

### Expected Result
The application should correctly handle the Recap marker and navigate to the expected playback position.

---

## TC_PLAYBACK_008 — Watch Credits Marker

**Test Type:** Functional Testing  
**Priority:** Medium

### Test Steps
1. Play content containing a Watch Credits marker.
2. Reach the end-credit section.
3. Verify the Watch Credits option.
4. Select the option.

### Expected Result
The application should correctly navigate to the relevant credits section.
