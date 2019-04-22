import maya.cmds as cmds
import functools
import mcake.generic_utils.ui_utils as uu

def createRiggingToolsUI():
    
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
        
    cmds.window( windowID, title="MCAKE: Animation & Rigging Tools", sizeable=False, resizeToFitChildren=True )
    
    cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[ (1,120), (2,120), (3,120) ], columnOffset=[ ] )
    
    cmds.text( label='Attribute Name:' )
    cnFld = cmds.textField( text='UrvaX2' )
    cmds.separator( h=10, style='none' )

    cmds.button( label='Mirror Rot Trans', command=functools.partial(eh_copy_vals, ['rx','ry','rz','tx','ty','tz'] ))
    cmds.button( label='Mirror Given', command=functools.partial(eh_mirror_given, cnFld))
    cmds.separator( h=10, style='none' )
    cmds.button( label='Mirror rx', command=functools.partial(eh_copy_vals, ['rx'] ))
    cmds.button( label='Mirror ry', command=functools.partial(eh_copy_vals, ['ry'] ))
    cmds.button( label='Mirror rz', command=functools.partial(eh_copy_vals, ['rz'] ))
    cmds.button( label='Mirror tx', command=functools.partial(eh_copy_vals, ['tx'] ))
    cmds.button( label='Mirror ty', command=functools.partial(eh_copy_vals, ['ty'] ))
    cmds.button( label='Mirror tz', command=functools.partial(eh_copy_vals, ['tz'] ))


    cmds.button( label='Copy Rot Trans', command=functools.partial(eh_mirror_vals, ['rx','ry','rz','tx','ty','tz'] ))
    cmds.button( label='Copy Given', command=functools.partial(eh_copy_given, cnFld))
    cmds.separator( h=10, style='none' )
    cmds.button( label='Copy rx', command=functools.partial(eh_mirror_vals, ['rx'] ))
    cmds.button( label='Copy ry', command=functools.partial(eh_mirror_vals, ['ry'] ))
    cmds.button( label='Copy rz', command=functools.partial(eh_mirror_vals, ['rz'] ))
    cmds.button( label='Copy tx', command=functools.partial(eh_mirror_vals, ['tx'] ))
    cmds.button( label='Copy ty', command=functools.partial(eh_mirror_vals, ['ty'] ))
    cmds.button( label='Copy tz', command=functools.partial(eh_mirror_vals, ['tz'] ))
    
    # Cancel button
    cmds.button( label='Cancel', command=functools.partial( g_cancelCallback, windowID))

    cmds.showWindow()

# Event Handlers
def g_cancelCallback(windowID,  *pArgs ):
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )

def eh_copy_given(fld):
    eh_copy_vals(uu.text_val(cnFld))

def eh_mirror_given(fld):
    eh_mirror_vals(uu.text_val(cnFld))

# copy([rx,ry,rz])
def eh_copy_vals(attrs):
    objs = cmds.ls(sl=True)
    if len(objs) == 0:
        return

    a = objs[0]
    b = objs[1]
    avals = []
    bvals = []

    for attr in attrs:
        ta = cmds.getAttr(a + '.' + attr)
        tb = cmds.getAttr(b + '.' + attr)
        cmds.setAttr(a + '.' + attr, tb)
        cmds.setAttr(b + '.' + attr, ta)

    print("Done key value swap for", attrs)

def eh_mirror_vals(attrs):
    objs = cmds.ls(sl=True)
    if len(objs) == 0:
        return

    a = objs[0]
    b = objs[1]
    avals = []
    bvals = []

    for attr in attrs:
        ta = cmds.getAttr(a + '.' + attr)
        tb = cmds.getAttr(b + '.' + attr)
        cmds.setAttr(a + '.' + attr, -tb)
        cmds.setAttr(b + '.' + attr, -ta)

    print("Done key value mirror for", attrs)


'''
# Event Handler
def eh_mirror_rot_trans(*pArgs):
    print("Mirror Keyable")
    objs = cmds.ls(sl=True)
    c = 0
    src = []
    target = []
    for obj in objs:
        if c == 0:
            src.append(cmds.getAttr("{0}.translateX".format(obj)))
            src.append(cmds.getAttr("{0}.translateY".format(obj)))
            src.append(cmds.getAttr("{0}.translateZ".format(obj)))
            src.append(cmds.getAttr("{0}.rotateX".format(obj)))
            src.append(cmds.getAttr("{0}.rotateY".format(obj)))
            src.append(cmds.getAttr("{0}.rotateZ".format(obj)))
            print("Source: " + obj)
        else:
            target.append(cmds.getAttr("{0}.translateX".format(obj)))
            target.append(cmds.getAttr("{0}.translateY".format(obj)))
            target.append(cmds.getAttr("{0}.translateZ".format(obj)))
            target.append(cmds.getAttr("{0}.rotateX".format(obj)))
            target.append(cmds.getAttr("{0}.rotateY".format(obj)))
            target.append(cmds.getAttr("{0}.rotateZ".format(obj)))
            print("Target: " + obj)
        c += 1
    
    c = 0
    for obj in objs:
        if c == 0:
            #cmds.setAttr("{0}.translateX".format(obj), -1 * target[0])
            cmds.setAttr("{0}.translateY".format(obj), target[1])
            cmds.setAttr("{0}.translateZ".format(obj), target[2])
            cmds.setAttr("{0}.rotateX".format(obj), target[3])
            cmds.setAttr("{0}.rotateY".format(obj), target[4])
            cmds.setAttr("{0}.rotateZ".format(obj), target[5])

            print("Copied to " + obj)
        else:
            #cmds.setAttr("{0}.translateX".format(obj), -1 * src[0])
            cmds.setAttr("{0}.translateY".format(obj), src[1])
            cmds.setAttr("{0}.translateZ".format(obj), src[2])
            cmds.setAttr("{0}.rotateX".format(obj), src[3])
            cmds.setAttr("{0}.rotateY".format(obj), src[4])
            cmds.setAttr("{0}.rotateZ".format(obj), src[5])

            print("Copied to " + obj)
        c += 1
    print("Mirror Keyable - Done")

def eh_mirror_rot(*pArgs):
    print("Mirror Keyable")
    objs = cmds.ls(sl=True)
    c = 0
    src = []
    target = []
    for obj in objs:
        if c == 0:
            src.append(cmds.getAttr("{0}.rotateX".format(obj)))
            src.append(cmds.getAttr("{0}.rotateY".format(obj)))
            src.append(cmds.getAttr("{0}.rotateZ".format(obj)))
            print("Source: " + obj)
        else:
            target.append(cmds.getAttr("{0}.rotateX".format(obj)))
            target.append(cmds.getAttr("{0}.rotateY".format(obj)))
            target.append(cmds.getAttr("{0}.rotateZ".format(obj)))
            print("Target: " + obj)
        c += 1
    
    c = 0
    for obj in objs:
        if c == 0:
            cmds.setAttr("{0}.rotateX".format(obj), target[1])
            cmds.setAttr("{0}.rotateY".format(obj), target[2])
            cmds.setAttr("{0}.rotateZ".format(obj), target[3])

            print("Copied to " + obj)
        else:
            cmds.setAttr("{0}.rotateX".format(obj), src[1])
            cmds.setAttr("{0}.rotateY".format(obj), src[2])
            cmds.setAttr("{0}.rotateZ".format(obj), src[3])

            print("Copied to " + obj)
        c += 1
    print("Mirror Keyable - Done")
'''