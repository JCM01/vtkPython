import vtk

#polydataSource = vtk.vtkSTLReader()
#polydataSource.SetFileName("SET HERE YOUR .STL")
#polydataSource.Update()

polydataSource = vtk.vtkSphereSource()
polydataSource.SetRadius(10)
polydataSource.SetThetaResolution(5)
polydataSource.SetPhiResolution(3)
polydataSource.Update()

# remove double vertices
cleanPolyData = vtk.vtkCleanPolyData()
cleanPolyData.SetInputData(polydataSource.GetOutput())
cleanPolyData.Update()

# create normals
normals = vtk.vtkPolyDataNormals()
normals.SetComputeCellNormals(1)
normals.SetInputData(cleanPolyData.GetOutput())
normals.SplittingOff()
normals.Update()

#Polydata into triangulation
polydata = vtk.vtkPolyData()
polydata.DeepCopy(normals.GetOutput())
numberOfPoints = polydata.GetNumberOfPoints()
print(polydata.GetNumberOfPoints())

# triangulate new connecting faces
triangleFilter = vtk.vtkTriangleFilter()
triangleFilter.SetInputData(polydata)
triangleFilter.Update()


# visualize
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(triangleFilter.GetOutput())
actor = vtk.vtkActor()
actor.GetProperty().SetEdgeVisibility(1)
actor.GetProperty().SetOpacity(0.5)
actor.GetProperty().BackfaceCullingOn()
# actor.GetProperty().SetRepresentationToWireframe()
actor.SetMapper(mapper)

camera = vtk.vtkCamera()
camera.SetPosition(1, 1, 1)
camera.SetFocalPoint(0, 0, 0)

renderer = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

renderer.AddActor(actor)
renderer.SetActiveCamera(camera)
renderer.ResetCamera()
renderer.SetBackground(1, 1, 1)

renWin.SetSize(300, 300)

renWin.Render()
iren.Start()
