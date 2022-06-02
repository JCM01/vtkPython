import vtk

# Sphere in yellow.
sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(5,0,0)
sphereSource.Update()
sphereSource = sphereSource.GetOutput() # vtkPolyData()

colors = vtk.vtkUnsignedCharArray()
colors.SetNumberOfComponents(3)
colors.SetNumberOfTuples(sphereSource.GetNumberOfCells())
for c in range(sphereSource.GetNumberOfCells()):
    colors.SetTuple(c, [255, 234, 0])
sphereSource.GetCellData().SetScalars(colors)

# Cone in blue
coneSource =vtk.vtkConeSource()
coneSource.Update()
coneSource = coneSource.GetOutput() # vtkPolyData()

colors = vtk.vtkUnsignedCharArray()
colors.SetNumberOfComponents(3)
colors.SetNumberOfTuples(coneSource.GetNumberOfCells())
for c in range(coneSource.GetNumberOfCells()):
    colors.SetTuple(c, [123, 145, 255])
coneSource.GetCellData().SetScalars(colors)

# Combine the two meshes
appendFilter = vtk.vtkAppendPolyData()
appendFilter.AddInputData(sphereSource)
appendFilter.AddInputData(coneSource)
appendFilter.Update()

# Create a mapper and actor
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(appendFilter.GetOutputPort())
mapper.SetColorModeToDirectScalars()

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer, render window, and interactor
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)


# Add the actors to the scene
back = vtk.vtkNamedColors()
renderer.AddActor(actor)
renderer.SetBackground(back.GetColor3d("Silver")) 

# Render and interact
renderWindow.Render()
renderWindowInteractor.Start()