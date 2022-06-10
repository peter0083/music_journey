/* =========================================================
 * ====                   WARNING                        ===
 * =========================================================
 * The code in this tab has been generated from the GUI form
 * designer and care should be taken when editing this file.
 * Only add/edit code inside the event handlers i.e. only
 * use lines between the matching comment tags. e.g.

 void myBtnEvents(GButton button) { //_CODE_:button1:12356:
     // It is safe to enter your event code here  
 } //_CODE_:button1:12356:
 
 * Do not rename this tab!
 * =========================================================
 */

public void panel1_Click1(GPanel source, GEvent event) { //_CODE_:panel1:490010:
  println("panel1 - GPanel >> GEvent." + event + " @ " + millis());
} //_CODE_:panel1:490010:

public void BranchValueSliderChange(GSlider source, GEvent event) { //_CODE_:BranchValueSlider:727545:
  //println("slider1 - GSlider >> GEvent." + event + " @ " + millis());
  MAXBRANCHVALUE = BranchValueSlider.getValueF();
} //_CODE_:BranchValueSlider:727545:

public void FFTBandsScaleSlider_change1(GSlider source, GEvent event) { //_CODE_:FFTBandsScaleSlider:835083:
   FFTBANDSCALE = FFTBandsScaleSlider.getValueF();
} //_CODE_:FFTBandsScaleSlider:835083:

public void FFTDecaySlider_change1(GSlider source, GEvent event) { //_CODE_:FFTDecaySlider:487922:
  FFTDecay = FFTDecaySlider.getValueF();
} //_CODE_:FFTDecaySlider:487922:

public void COLORFREQDIVISORSlider_change1(GSlider source, GEvent event) { //_CODE_:COLORFREQDIVISORSlider:557796:
  COLORFREQDIVISOR = COLORFREQDIVISORSlider.getValueF();
} //_CODE_:COLORFREQDIVISORSlider:557796:

public void ANGLEMULTIPLIERSlider_change1(GSlider source, GEvent event) { //_CODE_:ANGLEMULTIPLIERSlider:738625:
  ANGLEMULTIPLIER = ANGLEMULTIPLIERSlider.getValueF();
} //_CODE_:ANGLEMULTIPLIERSlider:738625:

public void BASESlider_change1(GSlider source, GEvent event) { //_CODE_:BASESlider:303729:
  BASE = BASESlider.getValueF();
} //_CODE_:BASESlider:303729:



// Create all the GUI controls. 
// autogenerated do not edit
public void createGUI(){
  G4P.messagesEnabled(false);
  G4P.setGlobalColorScheme(GCScheme.BLUE_SCHEME);
  G4P.setCursor(ARROW);
  surface.setTitle("Sketch Window");
  panel1 = new GPanel(this, 1440, 10, 150, 200, "Variables");
  panel1.setCollapsible(false);
  panel1.setDraggable(false);
  panel1.setText("Variables");
  panel1.setOpaque(false);
  panel1.addEventHandler(this, "panel1_Click1");
  BranchValueSlider = new GSlider(this, 0, 40, 150, 10, 10.0);
  BranchValueSlider.setShowValue(true);
  BranchValueSlider.setShowLimits(true);
  BranchValueSlider.setLimits(0.66, 0.0, 1.0);
  BranchValueSlider.setShowTicks(true);
  BranchValueSlider.setNumberFormat(G4P.DECIMAL, 2);
  BranchValueSlider.setOpaque(false);
  BranchValueSlider.addEventHandler(this, "BranchValueSliderChange");
  MaxBranchLable = new GLabel(this, 0, 20, 130, 20);
  MaxBranchLable.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  MaxBranchLable.setText("MAXBRANCHVALUE");
  MaxBranchLable.setOpaque(false);
  FFTBANDSCALELable = new GLabel(this, 0, 50, 130, 20);
  FFTBANDSCALELable.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  FFTBANDSCALELable.setText("FFTBANDSCALE");
  FFTBANDSCALELable.setOpaque(false);
  FFTBandsScaleSlider = new GSlider(this, 0, 70, 150, 10, 10.0);
  FFTBandsScaleSlider.setShowValue(true);
  FFTBandsScaleSlider.setShowLimits(true);
  FFTBandsScaleSlider.setLimits(40.0, 1.0, 200.0);
  FFTBandsScaleSlider.setShowTicks(true);
  FFTBandsScaleSlider.setNumberFormat(G4P.DECIMAL, 2);
  FFTBandsScaleSlider.setOpaque(false);
  FFTBandsScaleSlider.addEventHandler(this, "FFTBandsScaleSlider_change1");
  FFTDecaylable = new GLabel(this, 0, 80, 130, 20);
  FFTDecaylable.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  FFTDecaylable.setText("FFTDECAY");
  FFTDecaylable.setOpaque(false);
  FFTDecaySlider = new GSlider(this, 0, 100, 150, 10, 10.0);
  FFTDecaySlider.setShowValue(true);
  FFTDecaySlider.setShowLimits(true);
  FFTDecaySlider.setLimits(0.7, 0.0, 1.0);
  FFTDecaySlider.setShowTicks(true);
  FFTDecaySlider.setNumberFormat(G4P.DECIMAL, 2);
  FFTDecaySlider.setOpaque(false);
  FFTDecaySlider.addEventHandler(this, "FFTDecaySlider_change1");
  COLORFREQDIVISORLable = new GLabel(this, 0, 110, 130, 20);
  COLORFREQDIVISORLable.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  COLORFREQDIVISORLable.setText("COLORFREQDIVISOR");
  COLORFREQDIVISORLable.setOpaque(false);
  COLORFREQDIVISORSlider = new GSlider(this, 0, 130, 150, 10, 10.0);
  COLORFREQDIVISORSlider.setShowValue(true);
  COLORFREQDIVISORSlider.setShowLimits(true);
  COLORFREQDIVISORSlider.setLimits(50.0, 1.0, 900.0);
  COLORFREQDIVISORSlider.setShowTicks(true);
  COLORFREQDIVISORSlider.setNumberFormat(G4P.DECIMAL, 2);
  COLORFREQDIVISORSlider.setOpaque(false);
  COLORFREQDIVISORSlider.addEventHandler(this, "COLORFREQDIVISORSlider_change1");
  ANGLEMULTIPLIERLabel = new GLabel(this, 0, 140, 130, 20);
  ANGLEMULTIPLIERLabel.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  ANGLEMULTIPLIERLabel.setText("ANGLEMULTIPLIER");
  ANGLEMULTIPLIERLabel.setOpaque(false);
  ANGLEMULTIPLIERSlider = new GSlider(this, 0, 160, 150, 10, 10.0);
  ANGLEMULTIPLIERSlider.setShowValue(true);
  ANGLEMULTIPLIERSlider.setShowLimits(true);
  ANGLEMULTIPLIERSlider.setLimits(0.6, 0.0, 1.4);
  ANGLEMULTIPLIERSlider.setShowTicks(true);
  ANGLEMULTIPLIERSlider.setNumberFormat(G4P.DECIMAL, 2);
  ANGLEMULTIPLIERSlider.setOpaque(false);
  ANGLEMULTIPLIERSlider.addEventHandler(this, "ANGLEMULTIPLIERSlider_change1");
  BASELabel = new GLabel(this, 0, 170, 130, 20);
  BASELabel.setTextAlign(GAlign.CENTER, GAlign.MIDDLE);
  BASELabel.setText("BASE bin divisor");
  BASELabel.setOpaque(false);
  BASESlider = new GSlider(this, 0, 190, 150, 10, 10.0);
  BASESlider.setShowValue(true);
  BASESlider.setShowLimits(true);
  BASESlider.setLimits(2.7, 1.1, 20.0);
  BASESlider.setShowTicks(true);
  BASESlider.setNumberFormat(G4P.DECIMAL, 2);
  BASESlider.setOpaque(false);
  BASESlider.addEventHandler(this, "BASESlider_change1");
  panel1.addControl(BranchValueSlider);
  panel1.addControl(MaxBranchLable);
  panel1.addControl(FFTBANDSCALELable);
  panel1.addControl(FFTBandsScaleSlider);
  panel1.addControl(FFTDecaylable);
  panel1.addControl(FFTDecaySlider);
  panel1.addControl(COLORFREQDIVISORLable);
  panel1.addControl(COLORFREQDIVISORSlider);
  panel1.addControl(ANGLEMULTIPLIERLabel);
  panel1.addControl(ANGLEMULTIPLIERSlider);
  panel1.addControl(BASELabel);
  panel1.addControl(BASESlider);
}

// Variable declarations 
// autogenerated do not edit
GPanel panel1; 
GSlider BranchValueSlider; 
GLabel MaxBranchLable; 
GLabel FFTBANDSCALELable; 
GSlider FFTBandsScaleSlider; 
GLabel FFTDecaylable; 
GSlider FFTDecaySlider; 
GLabel COLORFREQDIVISORLable; 
GSlider COLORFREQDIVISORSlider; 
GLabel ANGLEMULTIPLIERLabel; 
GSlider ANGLEMULTIPLIERSlider; 
GLabel BASELabel; 
GSlider BASESlider; 
