# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 17:01:18 2016

@author: SMALLON
"""




IBB = ['AMGN','GILD','CELG','BIIB','REGN','MYL','ILMN','VRTX','ALXN','INCY','BMRN','MDVN','JAZZ',	'ALKS','SHPG','SGEN','ALNY','QGEN','UTHR','TSRO','NBIX','TECH','ENDP','ACAD','AKRX','ICPT','IONS','HZNP','JUNO','CBPO','LGND','PRAH','GRFS','MDCO','KITE','INCR','IPXL','MYGN','OPHT','NKTR','RARE','NVAX','EXEL','PRTA','IRWD','RDUS','BLUE','ONCE','AGIO','LXRX','ARIA','GWPH','PCRX','SAGE','PTLA','MCRB','ALDR','FPRX','INVA','XLRN','HALO','ACOR','ACHN','DEPO','FGEN','DERM','INSY','TBPH','CXRX','SRPT','CHRS','SUPN','MGNX','LMNX','AMAG','GHDX','RGEN','RLYP','CEMP','ADRO','MNTA','DBVT','FMI','AMPH','FOLD','XNCR','EGRX','SGNT','MACK','PACB','INSM','SGYP','ANIP','INO','CERS','RTRX','ATRA','AMRI','EPZM','PDLI','BPMC','CLVS','SCMP','NK','ARRY','XBIT','SCLN','FLML','RPTP','VNDA','LBIO','AERI','MNKD','CLDX','SPPI','OTIC','TLGT','FLXN','ARNA','OMER','GERN','PGNX','ENTA','AMRN','SGMO','RVNC','NDRM',	'BLCM','OMED','TRVN','ARDX','ARWR','CGEN','VSAR','AKBA','ADMS','NLNK','VTAE','COLL','AGTC','NSTG','CNCE','ESPR','IMGN','KPTI','PTCT','IMMU','PETX','ITEK','CCXI','BCRX','DRRX','FOMX','FLKS','ZGNX','RIGL','CRIS','VTL','CMRX','OVAS','RGLS','OSIR','QURE','EGLT','TTPH','NEOS','CASC','IMDZ','CARA','ECYT','AQXP','ANTH','OCUL','ADVM','ADHD','TKAI','SQNM','AFMD','ZFGN','INFI','LIFE','DRNA','CHMA','DNAI','KMPH','OREX','AEGR','USD']

SMBIx = IBB = ['AMGN','GILD','CELG','BIIB','REGN','MYL','ILMN','VRTX','ALXN','INCY','BMRN','MDVN','JAZZ',	'ALKS','SHPG','SGEN','ALNY','QGEN','UTHR','TSRO','NBIX','TECH','ENDP','ACAD','AKRX','ICPT','IONS','HZNP','JUNO','CBPO','LGND','PRAH','GRFS','MDCO','KITE','INCR','IPXL','MYGN','OPHT','NKTR','RARE','NVAX','EXEL','PRTA','IRWD','RDUS','BLUE','ONCE','AGIO','LXRX','ARIA','GWPH','PCRX','SAGE','PTLA','MCRB','ALDR','FPRX','INVA','XLRN','HALO','ACOR','ACHN','DEPO','FGEN','DERM','INSY','TBPH','CXRX','SRPT','CHRS','SUPN','MGNX','LMNX','AMAG','GHDX','RGEN','RLYP','CEMP','ADRO','MNTA','DBVT','FMI','AMPH','FOLD','XNCR','EGRX','SGNT','MACK','PACB','INSM','SGYP','ANIP','INO','CERS','RTRX','ATRA','AMRI','EPZM','PDLI','BPMC','CLVS','SCMP','NK','ARRY','XBIT','SCLN','FLML','RPTP','VNDA','LBIO','AERI','MNKD','CLDX','SPPI','OTIC','TLGT','FLXN','ARNA','OMER','GERN','PGNX','ENTA','AMRN','SGMO','RVNC','NDRM',	'BLCM','OMED','TRVN','ARDX','ARWR','CGEN','VSAR','AKBA','ADMS','NLNK','VTAE','COLL','AGTC','NSTG','CNCE','ESPR','IMGN','KPTI','PTCT','IMMU','PETX','ITEK','CCXI','BCRX','DRRX','FOMX','FLKS','ZGNX','RIGL','CRIS','VTL','CMRX','OVAS','RGLS','OSIR','QURE','EGLT','TTPH','NEOS','CASC','IMDZ','CARA','ECYT','AQXP','ANTH','OCUL','ADVM','ADHD','TKAI','SQNM','AFMD','ZFGN','INFI','LIFE','DRNA','CHMA','DNAI','KMPH','OREX','AEGR','USD']


from yahoo_finance import Share
for i in IBB:
    t = Share(i)
    book = float(t.get_book_value())
    if (book > 5.00):
        print(i,book,"Book value more than 5b")
    
        
from yahoo_finance import Share
for i in IBB:
    t = Share(i)
    P2S = (t.get_price_sales())
    print(P2S)
