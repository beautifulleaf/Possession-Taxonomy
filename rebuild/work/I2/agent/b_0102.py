import sys; sys.path.insert(0,'work/I2/agent')
from put import put
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":W+s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
kinds=[
{"n":"3D model","a":"3D model file","d":"A three-dimensional model held as a file to import into 3D tools.","t":["Character","Prop","Scene","OBJ","FBX","glTF","USD"],"s":"https://www.renderhub.com/3d-models?t=1","x":[
 A("Utah teapot","Martin Newell","1975","Utah_teapot","The standard reference model of computer graphics, drawn from a Melitta teapot at the University of Utah."),
 A("Stanford bunny","Greg Turk and Marc Levoy","1994","Stanford_bunny","Scan of a ceramic rabbit, 69,451 triangles, used to test graphics algorithms.")]},
{"n":"3D-printable model","a":"STL file · printable file","d":"A mesh file prepared to be sliced and printed on a 3D printer.","t":["STL (1987, 3D Systems)","3MF (3MF Consortium)","OBJ","AMF"],"s":W+"FDM_printing_file_formats","x":[
 A("3DBenchy","Creative Tools","2015","3DBenchy","Tugboat model by Daniel Norée and Paulo Kiefe made to test printer accuracy.",[
  ("3DBenchy STL","Creative Tools","2015","April 2015, originally CC-BY-ND"),
  ("3DBenchy multi-part, multi-colour","Creative Tools","2015","July 2015"),
  ("3DBenchy public domain","Creative Tools","2025","Moved to CC0 in February 2025")])]},
{"n":"Avatar model","a":"VRM · Live2D model · VTuber model","d":"A rigged character model for social VR or streaming.","t":["3D VRM","3D for VRChat","2D Live2D rig"],"s":W+"VRM","x":[
 A("VRM avatar","","","VRM","glTF-based 3D model format for virtual-reality and metaverse avatars."),
 A("Live2D model","Live2D Ltd.","2008","Live2D","Layered 2D character rigged for 2.5D motion, used with face tracking by VTubers.",[("Live2D Vector","Live2D Ltd.","2009","First application")])]},
{"n":"3D material","a":"shader","d":"A surface material or shader definition for 3D rendering.","t":["PBR texture set","Procedural shader"],"s":"https://app.cinevva.com/guides/free-textures-hdris-materials"},
{"n":"HDRI and environment map","a":"HDRI · environment map","d":"An environment lighting map or light setup for 3D rendering.","t":["Studio","Outdoor","Interior"],"s":"https://app.cinevva.com/guides/free-textures-hdris-materials","x":[
 A("HDR light probe lighting","Paul Debevec","1997","High-dynamic-range_rendering","High-dynamic-range image of a place used to light a rendered scene.",[("Radiance HDR format","Greg Ward","1985","First file format to hold a high-dynamic-range image")])]},
]
put('I2','01_02',{"kinds":kinds,"brands":[],"traditions":[],"notes":"Dropped the single RenderHub SKU (Military Avatar - Bundle); the avatar mention moved to the new Avatar model kind. No Poly Haven, Quixel Megascans or VRChat base-body archetypes: no retrieved page named them. VRM maker not stated on the fetched page, so mk blank. Suzanne page redirected to Blender and was not used."})
