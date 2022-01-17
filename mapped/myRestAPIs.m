temp(req);
 new res,timdat
 S cnt=0
 S timdat=""
 F  S timdat=$O(^SENSORS("temp",timdat)) Q:timdat=""  D
 . set cnt=cnt+1
 . set res(cnt,"time")=timdat
 . set res(cnt,"temp")=^SENSORS("temp",timdat)
 QUIT $$response^%zmgweb(.res)
humid(req);
 new res,timdat
 S timdat=""
 S cnt=0
 F  S timdat=$O(^SENSORS("humid",timdat)) Q:timdat=""  D
 . set cnt=cnt+1
 . set res(cnt,"time")=timdat
 . set res(cnt,"humid")=^SENSORS("humid",timdat)
 QUIT $$response^%zmgweb(.res)

