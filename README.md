# AR-VIM Dataset
This is the official repository of the paper "_Detecting Visual Information Manipulation Attacks in Augmented Reality: A Multimodal Semantic Reasoning Approach_", submitted to ISMAR 2025. It introduces **AR-VIM**, a dataset of 306 raw-AR video pairs. 

## Dataset Description

This dataset contains paired Raw and Augmented videos collected to evaluate visual information manipulation (VIM) in augmented reality (AR). Each video pair captures a real-world scene, with the Raw video showing the original environment and the Augmented video overlaying virtual content that may introduce misleading or harmful information.

The dataset is structured around two key taxonomies:

  - **Attack Format**: what aspect of visual information is altered

  - **Attack Purpose**: the intention or effect of the manipulation

### Attack Formats

  - Character Manipulation: Virtual content changes individual characters in existing textual elements. 
  - Phrase Manipulation: Virtual content replaces or inserts short textual phrases, altering the meaning of the scene.
  - Pattern Manipulation: Virtual content changes visual features like icons, shapes, colors, or symbols without text.

### Attack Purposes

  - Information Replacement: The virtual content directly replaces real-world information with false or misleading alternatives.
  - Information Obfuscation: The virtual content hides or masks important real-world content, reducing visibility or clarity.
  - Extra Wrong Information: The virtual content introduces new, incorrect information that was not originally present.

<figure>
  <img src="imgs/datasethd.png" alt="Description" width="1200"/>
  <figcaption align="center"><b>Figure 1.</b> Samples from the AR-VIM dataset. Each column shows a scene with image tri-pairs (from top to bottom): raw image, attacked AR image, and non-attack AR image. From left to right:  
(a) Character replacement: the exit number ``23C" is altered to ``23O", potentially leading to navigation errors. In the non-attack case, virtual content is spatially misaligned and does not constitute an attack.
(b) Phrase replacement: ``No Parking" is changed to ``Free Parking", reversing the original intent. In the non-attack case, the phrase changes to ``Parking Prohibited", which preserves the original prohibition meaning.  
(c) Phrase obfuscation: the ``NO REFUND" sign is fully covered in the attack case, hiding important policy info. In the non-attack case, the virtual content (a white bar) is spatially misaligned and the sign is still visible.
(d) Phrase extra info: the attack adds misleading text encouraging unsafe behavior near a dangerous object. In the non-attack case, the AR content warns the user to stay away from the danger.  
(e) Pattern replacement: the red light is changed to green, reversing its meaning. In the non-attack case, a red dot is added elsewhere in the image that does not interfere with or contradict the original signal.
(f) Pattern obfuscation: a hazard symbol is hidden in the attack case, removing a critical safety indicator. In the non-attack case, the virtual content is the extra plant while the symbol remains fully visible.  
(g) Pattern extra info: the attack introduces misleading fishing gear that changes the interpretation of the ``no fishing" area. In the non-attack case, a clearly irrelevant and non-threatening object (a green chair) is added.</figcaption>
</figure>

### Video Description

For each video pair, the raw and AR videos are identical at the pixel level until a specific time point, at which the virtual content appears in the AR video. This virtual content may or may not result in a visual information manipulation attack.

<div style="display: flex; gap: 20px;">
  <div style="flex: 1; text-align: center;">
    <video width="100%" autoplay loop muted playsinline>
      <source src="imgs/Augmented_Recordings_A_004.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <p><b>Raw Video</b></p>
  </div>
  <div style="flex: 1; text-align: center;">
    <video width="100%" autoplay loop muted playsinline>
      <source src="imgs/Raw_Recordings_A_004.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <p><b>Augmented Video</b></p>
  </div>
</div>



### Video Details

  - Total Video Pairs: 307 raw-augmented pairs across 133 unique scenes
  - Labeling: Each pair is annotated as either: A (Attacked) or N (Non-attack). The labels are in the videos' names.
  - Format: .mp4
  - Resolution: 480 × 1080 pixels
  - Frame Rate: 15 FPS

## Dataset Structure

The dataset can be accesssed through this [link](https://drive.google.com/drive/folders/1TbgY8RNR3sg3H1ItCSYenpZ3MRjmZlIC?usp=drive_link).

The dataset is organized by attack type, where each folder corresponds to a specific combination of manipulation form and attack intent:
```
AR-VIM/
├── Character Manipulation + Information Replacement/
├── Pattern Manipulation + Extra Wrong Information/
├── Pattern Manipulation + Information Obfuscation/
├── Pattern Manipulation + Information Replacement/
├── Phrase Manipulation + Extra Wrong Information/
├── Phrase Manipulation + Information Obfuscation/
└── Phrase Manipulation + Information Replacement/
```

Inside each folder, video files follow the naming convention:

**\{VideoType\}_Recordings\_\{AttackLabel\}\_\{XXX\}.mp4**

where:

  - {VideoType}: Either Raw or Augmented

  - {AttackLabel}: A for attack, N for non-attack

  - {XXX}: A 3-digit index, starting from 001

For example；

```
Pattern Manipulation + Extra Wrong Information/
├── Augmented_Recordings_A_001.mp4
├── Augmented_Recordings_A_002.mp4
├── ...
├── Augmented_Recordings_N_001.mp4
├── ...
├── Raw_Recordings_A_001.mp4
├── Raw_Recordings_A_002.mp4
├── ...
├── Raw_Recordings_N_001.mp4
└── ...
```




