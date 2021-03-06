# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
"""Basic example which iterates through the tasks specified and
evaluates the given model on them.

For example:
`python examples/eval_model.py -t "babi:Task1k:2" -m "repeat_label"`
or
`python examples/eval_model.py -t "#CornellMovie" -m "ir_baseline" -mp "-lp 0.5"`
"""
from parlai.scripts.eval_model import setup_args, eval_model
import socket

if __name__ == '__main__':
    parser = setup_args()
    opt = parser.parse_args(print_args=False)
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR  , 1)
    sock.bind(("server ip",8061))
    sock.listen(5)
    conn, addr = sock.accept()

    eval_model(opt, conn, print_parser=parser)

    conn.send(bytes("exit\n" ,encoding="utf8"))
    conn.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
