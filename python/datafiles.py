import os

# Directories
datafile = "../data"
figdir = "../figures"
figdirleaflet = "../leaflet/images/"
datadirleaflet = "../leaflet/data/"

if not(os.path.exists(figdir)):
    os.makedirs(figdir)
if not(os.path.exists(figdirleaflet)):
    os.makedirs(figdirleaflet)
if not(os.path.exists(datadirleaflet)):
    os.makedirs(datadirleaflet)

# domain
coordinates1 = [-6.75, 3.001, 34.75, 40.0]
coordinates2 = [-1.0, -0.25, 36.65, 37.25]
coordinates3 = [-6.0, -5.25, 35.8, 36.2]
resolution1 = [1.0, 1.0]
resolution2 = [0.25, 0.25]

# local files
coastfile = os.path.join(datafile, "coastline_f.dat")
altimetryfile = os.path.join(datafile, "alborex_mean_sla.nc")
ctdlegs = [os.path.join(datafile, "ctd_positions_Leg1.txt"),
           os.path.join(datafile, "ctd_positions_Leg2.txt")
           ]
sstfile = [os.path.join(datafile, "A2014145125000.L2_LAC_SST.nc"),
           os.path.join(datafile, "A2014150020500.L2_LAC_SST.nc")
           ]
frontfile = os.path.join(datafile, "front_coordinates.dat")

# Remote files
adcpfile = "http://thredds.socib.es/thredds/dodsC/research_vessel/current_profiler/socib_rv-scb_rdi001/L1/2014/dep0023_socib-rv_scb-rdi001_L1_2014-05.nc"
ctdfile = "http://thredds.socib.es/thredds/dodsC/research_vessel/ctd/socib_rv-scb_sbe9002/L1_corr/2014/dep0007_socib-rv_scb-sbe9002_L1_corr_2014-05-25.nc",
gliderfiles = ["http://thredds.socib.es/thredds/dodsC/auv/glider/icoast00-ime_slcost000/L1/2014/dep0005_icoast00_ime-slcost000_L1_2014-05-25_data_dt.nc",
               "http://thredds.socib.es/thredds/dodsC/auv/glider/ideep00-ime_sldeep000/L1/2014/dep0012_ideep00_ime-sldeep000_L1_2014-05-25_data_dt.nc"]
profilerfiles: ["http://thredds.socib.es/thredds/dodsC/drifter/profiler_drifter/profiler_drifter_arvora3001-ogs_arvora3001/L1/2014/dep0001_profiler-drifter-arvora3001_ogs-arvora3001_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/profiler_drifter/profiler_drifter_provbioll001-ogs_provbioll001/L1/2014/dep0001_profiler-drifter-provbioll001_ogs-provbioll001_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/profiler_drifter/profiler_drifter_arvorc001-ime_arvorc001/L1/2014/dep0001_profiler-drifter-arvorc001_ime-arvorc001_L1_2014-05-25.nc"]
drifterfiles = ["http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp018-scb_svp013/L1/2014/dep0001_drifter-svp018_scb-svp013_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp019-scb_svp014/L1/2014/dep0001_drifter-svp019_scb-svp014_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp020-scb_svp015/L1/2014/dep0001_drifter-svp020_scb-svp015_L1_2014-05-28.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp021-scb_svp016/L1/2014/dep0001_drifter-svp021_scb-svp016_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp022-scb_svp017/L1/2014/dep0001_drifter-svp022_scb-svp017_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp024-scb_svp019/L1/2014/dep0001_drifter-svp024_scb-svp019_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp025-scb_svp020/L1/2014/dep0001_drifter-svp025_scb-svp020_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp027-scb_svp022/L1/2014/dep0001_drifter-svp027_scb-svp022_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp036-ime_svp007/L1/2014/dep0001_drifter-svp036_ime-svp007_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp037-ime_svp008/L1/2014/dep0001_drifter-svp037_ime-svp008_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp038-ime_svp009/L1/2014/dep0001_drifter-svp038_ime-svp009_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp039-ime_svp010/L1/2014/dep0001_drifter-svp039_ime-svp010_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp040-ime_svp011/L1/2014/dep0001_drifter-svp040_ime-svp011_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp041-ime_svp012/L1/2014/dep0001_drifter-svp041_ime-svp012_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp042-ime_svp006/L1/2014/dep0001_drifter-svp042_ime-svp006_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp043-ogs_svp001/L1/2014/dep0001_drifter-svp043_ogs-svp001_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp044-ogs_svp002/L1/2014/dep0001_drifter-svp044_ogs-svp002_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp045-ogs_svp003/L1/2014/dep0001_drifter-svp045_ogs-svp003_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp046-ogs_svp004/L1/2014/dep0001_drifter-svp046_ogs-svp004_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp047-ogs_svp005/L1/2014/dep0001_drifter-svp047_ogs-svp005_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp048-ime_svp013/L1/2014/dep0001_drifter-svp048_ime-svp013_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp049-ime_svp014/L1/2014/dep0001_drifter-svp049_ime-svp014_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp051-ime_svp016/L1/2014/dep0001_drifter-svp051_ime-svp016_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp052-ime_svp017/L1/2014/dep0001_drifter-svp052_ime-svp017_L1_2014-05-25.nc",
                "http://thredds.socib.es/thredds/dodsC/drifter/surface_drifter/drifter_svp054-ime_svp019/L1/2014/dep0001_drifter-svp054_ime-svp019_L1_2014-05-25.nc"]
rvfile = "http://thredds.socib.es/thredds/dodsC/research_vessel/gps/socib_rv-scb_pos001/L1/2014/05/dep0015_socib-rv_scb-pos001_L1_2014-05-25.nc"
thermosalfile = "http://thredds.socib.es/thredds/dodsC/research_vessel/thermosalinometer/socib_rv-scb_tsl001/L1/2014/05/dep0015_socib-rv_scb-tsl001_L1_2014-05-25.nc"
sstremotefiles =  ["https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/A2014145125000.L2_LAC_SST.nc",
                   "https://oceandata.sci.gsfc.nasa.gov/cgi/getfile/A2014150020500.L2_LAC_SST.nc"]
