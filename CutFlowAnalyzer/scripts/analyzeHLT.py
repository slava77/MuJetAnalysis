from ROOT import *

def analyzeHLT():
    files = {}
    files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV'] = "/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_0_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_2_1Aa.root"
    files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_02_8TeV'] = "/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_02_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_02_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_1_t1W.root"
    files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV'] = "/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_2_mjw.root"
    files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV'] = "/eos/uscms/store/user/lpcgem/dildick/dildick/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_RAW/DarkSUSY_mH_125_mGammaD_0400_ctauExp_2_8TeV_madgraph452_bridge224_LHE_pythia6_ANA/d37f287c329e62f6cda917e97d6b627b/out_cutana_1_1_Y38.root"
    f = TFile.Open(files['DarkSUSY_mH_125_mGammaD_0400_ctauExp_05_8TeV'])
    f.cd("cutFlowAnalyzer")      
    f.ls()

    t = f.Get("cutFlowAnalyzer/Events");
    
    nentries = t.GetEntries();
    m_events = 0
    m_events4GenMu = 0
    m_events1GenMu17 = 0
    m_events2GenMu8 = 0      
    m_events3GenMu8 = 0
    m_events4GenMu8 = 0
    m_events1SelMu17 = 0
    m_events2SelMu8 = 0
    m_events3SelMu8 = 0
    m_events4SelMu8 = 0
    m_events2MuJets = 0
    m_events2DiMuons = 0
    
    m_events2DiMuonsDzOK_FittedVtx = 0
    m_events2DiMuonsDzOK_ConsistentVtx = 0

    m_events2DiMuonsMassOK_FittedVtx_noHLT = 0
    m_events2DiMuonsMassOK_ConsistentVtx_noHLT = 0
    m_events2DiMuonsIsoTkOK_FittedVtx_noHLT = 0
    m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT = 0
    m_eventsVertexOK_FittedVtx_noHLT = 0
    m_eventsVertexOK_ConsistentVtx_noHLT = 0

    m_eventsDiMuonHLTFired_FittedVtx = 0
    m_eventsDiMuonHLTFired_ConsistentVtx = 0
    m_events2DiMuonsMassOK_FittedVtx = 0
    m_events2DiMuonsMassOK_ConsistentVtx = 0
    m_events2DiMuonsIsoTkOK_FittedVtx = 0
    m_events2DiMuonsIsoTkOK_ConsistentVtx = 0

    m_eventsVertexOK_FittedVtx = 0
    m_eventsVertexOK_ConsistentVtx = 0

    m_eventsFailingHLT = 0
    m_isDiMuonHLTFired = 0

    text_file = open("Output.txt", "w")
    text_file2 = open("lxy.txt", "w")

    for k in range(0,nentries):
        t.GetEntry(k)    
        m_events += 1

        if (t.isDiMuonHLTFired):
            m_isDiMuonHLTFired += 1
        if (t.is4GenMu):
            m_events4GenMu += 1            
        if (t.is1GenMu17):
            m_events1GenMu17 += 1
            if (t.is2GenMu8):
                m_events2GenMu8 += 1      
            if (t.is3GenMu8):
                m_events3GenMu8 += 1
            if (t.is4GenMu8):
                m_events4GenMu8 += 1
        if (t.is1SelMu17):
            m_events1SelMu17 += 1
            if (t.is2SelMu8):
                m_events2SelMu8 += 1
            if (t.is3SelMu8):
                m_events3SelMu8 += 1
            if (t.is4SelMu8):
                m_events4SelMu8 += 1
                
        if (t.is2MuJets):
            m_events2MuJets += 1
            if (t.is2DiMuons):
                m_events2DiMuons += 1
                
                if (t.is2DiMuonsDzOK_FittedVtx):
                    m_events2DiMuonsDzOK_FittedVtx += 1
                    if (t.is2DiMuonsMassOK_FittedVtx):
                        m_events2DiMuonsMassOK_FittedVtx_noHLT += 1
                        if (t.is2DiMuonsIsoTkOK_FittedVtx):
                            m_events2DiMuonsIsoTkOK_FittedVtx_noHLT += 1
                            if (t.isVertexOK):
                                m_eventsVertexOK_FittedVtx_noHLT += 1
                                if (not t.isDiMuonHLTFired):                                    
                                    m_eventsFailingHLT += 1
                                    text_file.write("'%s:%s:%s',"%(t.run, t.lumi, t.event))
                                    text_file2.write("%s\t%s\n"%(t.genA0_Lxy, t.genA1_Lxy))
#                                    text_file2.write("%s\n"%(t.genA1_Lxy))
                                    print t.genA0_Lxy
#                                    print "genA0_Lxy", t.genA0_Lxy, "genA1_Lxy", t.genA1_Lxy

                    if (t.isDiMuonHLTFired):
                        m_eventsDiMuonHLTFired_FittedVtx += 1
                        if (t.is2DiMuonsMassOK_FittedVtx):
                            m_events2DiMuonsMassOK_FittedVtx += 1
                            if (t.is2DiMuonsIsoTkOK_FittedVtx):
                                m_events2DiMuonsIsoTkOK_FittedVtx += 1
                                if (t.isVertexOK):
                                    m_eventsVertexOK_FittedVtx += 1
                                    
                if (t.is2DiMuonsDzOK_ConsistentVtx):
                    m_events2DiMuonsDzOK_ConsistentVtx += 1
                    if (t.is2DiMuonsMassOK_ConsistentVtx):
                        m_events2DiMuonsMassOK_ConsistentVtx_noHLT += 1
                        if (t.is2DiMuonsIsoTkOK_ConsistentVtx):
                            m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT += 1
                            if (t.isVertexOK):
                                m_eventsVertexOK_ConsistentVtx_noHLT += 1
                    if (t.isDiMuonHLTFired):
                        m_eventsDiMuonHLTFired_ConsistentVtx += 1
                        if (t.is2DiMuonsMassOK_ConsistentVtx):
                            m_events2DiMuonsMassOK_ConsistentVtx += 1
                            if (t.is2DiMuonsIsoTkOK_ConsistentVtx):
                                m_events2DiMuonsIsoTkOK_ConsistentVtx += 1
                                if (t.isVertexOK):
                                    m_eventsVertexOK_ConsistentVtx += 1
                                    
    print "m_events", m_events
    print "m_isDiMuonHLTFired", m_isDiMuonHLTFired
    print "m_events4GenMu", m_events4GenMu
    print "m_events1GenMu17", m_events1GenMu17
    print "m_events2GenMu8", m_events2GenMu8
    print "m_events3GenMu8", m_events3GenMu8
    print "m_events4GenMu8", m_events4GenMu8
    print "m_events1SelMu17", m_events1SelMu17
    print "m_events2SelMu8", m_events2SelMu8
    print "m_events3SelMu8", m_events3SelMu8
    print "m_events4SelMu8", m_events4SelMu8

    print "m_events2MuJets", m_events2MuJets
    print "m_events2DiMuons", m_events2DiMuons

    print "m_events2DiMuonsDzOK_FittedVtx", m_events2DiMuonsDzOK_FittedVtx
    print "m_events2DiMuonsDzOK_ConsistentVtx", m_events2DiMuonsDzOK_ConsistentVtx
    
    print "m_events2DiMuonsMassOK_FittedVtx_noHLT", m_events2DiMuonsMassOK_FittedVtx_noHLT
    print "m_events2DiMuonsIsoTkOK_FittedVtx_noHLT", m_events2DiMuonsIsoTkOK_FittedVtx_noHLT
    print "m_eventsVertexOK_FittedVtx_noHLT", m_eventsVertexOK_FittedVtx_noHLT
    print
    print "m_events2DiMuonsMassOK_FittedVtx", m_events2DiMuonsMassOK_FittedVtx
    print "m_events2DiMuonsIsoTkOK_FittedVtx", m_events2DiMuonsIsoTkOK_FittedVtx
    print "m_eventsVertexOK_FittedVtx", m_eventsVertexOK_FittedVtx
    print
    print "m_events2DiMuonsMassOK_ConsistentVtx_noHLT", m_events2DiMuonsMassOK_ConsistentVtx_noHLT
    print "m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT", m_events2DiMuonsIsoTkOK_ConsistentVtx_noHLT
    print "m_eventsVertexOK_ConsistentVtx_noHLT", m_eventsVertexOK_ConsistentVtx_noHLT
    print
    print "m_events2DiMuonsMassOK_ConsistentVtx", m_events2DiMuonsMassOK_ConsistentVtx
    print "m_events2DiMuonsIsoTkOK_ConsistentVtx", m_events2DiMuonsIsoTkOK_ConsistentVtx
    print "m_eventsVertexOK_ConsistentVtx", m_eventsVertexOK_ConsistentVtx
    print
    print "m_eventsFailingHLT", m_eventsFailingHLT

    text_file.close()
    text_file2.close()


    
if __name__ == "__main__":
    analyzeHLT()
