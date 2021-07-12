import skeletor as sk


mesh = sk.example_mesh()
fixed = sk.pre.fix_mesh(mesh, remove_disconnected=5, inplace=False)
skel = sk.skeletonize.by_wavefront(fixed, waves=1, step_size=1)
skel
skel.show(mesh=False)
