def spectrum(x):
    from datetime import datetime, date
    with open(x, "rb") as f:
        byte = f.read(3)
        spectrum.etime=0
        weight=1
        for b in byte:
          spectrum.etime = spectrum.etime + weight * (b&15);
          weight = 10 * weight;
          spectrum.etime = spectrum.etime + weight * ((b<<4)&15);
          weight = 10 * weight;
        spectrum.ltimeflag = int.from_bytes(f.read(1), byteorder='little');
        spectrum.rtimeflag = int.from_bytes(f.read(1), byteorder='little');
        spectrum.convergain = int.from_bytes(f.read(1), byteorder='little');
        spectrum.digoffset = int.from_bytes(f.read(1), byteorder='little');
        spectrum.idcodestr = str(f.read(15), 'utf-8');
        spectrum.pca_date = str(f.read(12), 'utf-8');
        spectrum.pca_time = str(f.read(12), 'utf-8');
        spectrum.group = int.from_bytes(f.read(1), byteorder='little');
        spectrum.units = int.from_bytes(f.read(1), byteorder='little');
        spectrum.cal = f.read(110);
        cal=[]
        for b in spectrum.cal:
            cal.append(b)
        spectrum.calib=cal
        spectrum.exp = f.read(99);
        exp=[]
        for b in spectrum.exp:
            exp.append(b)
        spectrum.expansion=exp
        spectrum.phamode = int.from_bytes(f.read(1), byteorder='big');
        spectrum.mcs = int.from_bytes(f.read(1), byteorder='big');
        spectrum.mcstimelab = int.from_bytes(f.read(1), byteorder='big');
        spectrum.mcsdwellnumb = int.from_bytes(f.read(1), byteorder='big');
        spectrum.mcsa = f.read(3);
        mcsa=[]
        for b in spectrum.mcsa:
            mcsa.append(b)
        spectrum.mcspasct=mcsa
        spectrum.centupflag = int.from_bytes(f.read(1), byteorder='big');
        spectrum.fwhmflag = int.from_bytes(f.read(1), byteorder='big');
        spectrum.numbchanspm = int.from_bytes(f.read(2), byteorder='little');
        spectrum.asday = int.from_bytes(f.read(1), byteorder='big');
        spectrum.asmonth = int.from_bytes(f.read(1), byteorder='big');
        spectrum.asyear = int.from_bytes(f.read(2), byteorder='little');
        spectrum.ashund = int.from_bytes(f.read(1), byteorder='big');
        spectrum.assec = int.from_bytes(f.read(1), byteorder='big');
        spectrum.asmin = int.from_bytes(f.read(1), byteorder='big');
        spectrum.ashour = int.from_bytes(f.read(1), byteorder='big');
        spectrum.astpday = int.from_bytes(f.read(1), byteorder='big');
        spectrum.astpmonth = int.from_bytes(f.read(1), byteorder='big');
        spectrum.astpyear = int.from_bytes(f.read(2), byteorder='little');
        spectrum.astphund = int.from_bytes(f.read(1), byteorder='big');
        spectrum.astpsec = int.from_bytes(f.read(1), byteorder='big');
        spectrum.astpmin = int.from_bytes(f.read(1), byteorder='big');
        spectrum.astphour = int.from_bytes(f.read(1), byteorder='big');
        spectrum.id = str(f.read(72), 'utf-8');
        spectrum.majvers = int.from_bytes(f.read(1), byteorder='big');
        spectrum.minvers = int.from_bytes(f.read(1), byteorder='big');
        spectrum.real_elap_time = int.from_bytes(f.read(3), byteorder='little');
        spectrum.acqstop_time = str(f.read(13), 'utf-8');
        spectrum.acqstop_date = str(f.read(13), 'utf-8');
        spectrum.acqstart_time = str(f.read(13), 'utf-8');
        spectrum.acqstart_date = str(f.read(13), 'utf-8');
        g = f.read(1)
        spectrum.fut = f.read(96);
        fut=[]
        for b in spectrum.fut:
            fut.append(b)
        spectrum.future=fut
        spectrum.endheader = int.from_bytes(f.read(2), byteorder='little');
        if (100*spectrum.majvers + spectrum.minvers != spectrum.endheader):
            print ('get_spectrum_spm:headerError','Error reading header ... version mismatch')
        hund = spectrum.ashund/100.0;
        spectrum.acquire_start = 24*3600*date.toordinal(datetime(spectrum.asyear,spectrum.asmonth,spectrum.asday,spectrum.ashour,spectrum.asmin,spectrum.assec))+hund;
        hund = spectrum.astphund/100.0;
        spectrum.acquire_stop = 24*3600*date.toordinal(datetime(spectrum.astpyear,spectrum.astpmonth,spectrum.astpday,spectrum.astphour,spectrum.astpmin,spectrum.astpsec))+hund;
        spectrum.data=[];
        for b in range(0, spectrum.numbchanspm):
            data = int.from_bytes(f.read(4), byteorder='little');
            spectrum.data.append(data)
        return (spectrum.data)
