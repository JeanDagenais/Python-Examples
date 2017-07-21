import inspect
import linecache

def trace_line_v2(frame, event, arg):
    if event != 'line':
        return

    # print '\n----- trace_line ----------------------------------------------'
    # print 'frame:                           %s' % frame
    # print 'event:                           %s' % event
    # print 'arg:                             %s' % arg
    #
    # print 'frame:                           %s' % frame
    # print 'frame.f_code:                    %s' % frame.f_code
    # print 'frame.f_code.co_name:            %s' % frame.f_code.co_name
    # print 'frame.f_code.co_filename:        %s' % frame.f_code.co_filename
    # print 'frame.f_lineno:                  %s' % frame.f_lineno

    line_number = frame.f_lineno
    line = linecache.getline(frame.f_code.co_filename, frame.f_lineno)
    # print 'line:                            %s' % line
    # name = frame.f_globals['__name__']
    print '  %s:%d  %s' % (frame.f_code.co_name, line_number, line.rstrip())

    # for line in traceback.format_stack():
    #     print(line.strip())

    # if event != 'line':
    #    return
    # co = frame.f_code
    # func_name = co.co_name
    # line_no = frame.f_lineno
    # filename = co.co_filename
    # print '  %s line %s' % (func_name, line_no)


def trace_service_v2(frame, event, arg):
    if event != 'call':
        return

    if frame.f_code.co_name == '_remove':
        return

    if not 'pydev/dev' in frame.f_code.co_filename:
        return

    # print '\n----- trace_call ----------------------------------------------'
    # print 'frame:                           %s' % frame
    # print 'event:                           %s' % event
    # print 'arg:                             %s' % arg
    #
    # print 'frame:                           %s' % frame
    # print 'frame.f_code:                    %s' % frame.f_code
    # print 'frame.f_code.co_name:            %s' % frame.f_code.co_name
    # print 'frame.f_code.co_filename:        %s' % frame.f_code.co_filename
    # print 'frame.f_lineno:                  %s' % frame.f_lineno
    #
    # print 'frame.f_back:                    %s' % frame.f_back
    # print 'frame.f_back.f_code:             %s' % frame.f_back.f_code
    # print 'frame.f_back.f_code.co_name:     %s' % frame.f_back.f_code.co_name
    # print 'frame.f_back.f_code.co_filename: %s' % frame.f_back.f_code.co_filename
    # print 'frame.f_back.f_lineno:           %s' % frame.f_back.f_lineno

    print '\n#', frame.f_code.co_name
    print 'Call to %s on line %s of %s' % (frame.f_code.co_name, frame.f_lineno, frame.f_code.co_filename)

    args, _, _, values = inspect.getargvalues(frame)
    #print ' arguments for functi "%s"' % inspect.getframeinfo(frame)[2]
    print ' arguments'
    for i in args:
        print "    %s = %s" % (i, values[i])

    # print 'calling trace_lines'
    return trace_line_v2

    return
