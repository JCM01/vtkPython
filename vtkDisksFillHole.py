import vtk

# create source

source = vtk.vtkDiskSource()
source.SetInnerRadius(1)
source.SetOuterRadius(2)
source.SetRadialResolution(100)
source.SetCircumferentialResolution(100)
source.Update()

#Same second source

source_2 = vtk.vtkDiskSource()
source_2.SetInnerRadius(1)
source_2.SetOuterRadius(2)
source_2.SetRadialResolution(100)
source_2.SetCircumferentialResolution(100)
source_2.Update()

#Define transform

transform = vtk.vtkTransform()
transform.Translate(0,0,1)

#Apply Filter

transform_filter = vtk.vtkTransformPolyDataFilter()
transform_filter.SetInputConnection(source_2.GetOutputPort())
transform_filter.SetTransform(transform)
transform_filter.Update()

#Merge polydata

mergepolydata = vtk.vtkAppendPolyData()
mergepolydata.AddInputData(source.GetOutput())
mergepolydata.AddInputData(transform_filter.GetOutput())
mergepolydata.Update()

#Clean Polydata

clean = vtk.vtkCleanPolyData()
clean.SetInputConnection(mergepolydata.GetOutputPort())
clean.Update()

#Apply fill holes filter to close surface

fill = vtk.vtkFillHolesFilter()
fill.SetInputConnection(clean.GetOutputPort())
fill.SetHoleSize(2)
fill.Update()

# mapper

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(fill.GetOutput())

# actor

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# create a rendering window and renderer
colors = vtk.vtkNamedColors()
ren = vtk.vtkRenderer()
ren.SetBackground(colors.GetColor3d("Silver"))
renWin = vtk.vtkRenderWindow()
renWin.SetWindowName("DICOM EN 3D")
renWin.AddRenderer(ren)

# create a renderwindowinteractor

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# assign actor to the renderer

ren.AddActor(actor)

# enable user interface interactor

iren.Initialize()
renWin.Render()
iren.Start()