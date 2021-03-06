# Copyright (C) 2016-2018 Alibaba Group Holding Limited
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from xdl.python import pybind

class TensorShape(object):
  def __init__(self, shape):
    self._dims = [shape[i] for i in range(len(shape))]

  def __repr__(self):
    return "TensorShape({0})".format(repr(self._dims))

  def __str__(self):
    return "TensorShape({0})".format(repr(self._dims))

  def __len__(self):
    return len(self._dims)

  def __getitem__(self, idx):
    return self._dims[idx]

  def dims(self):
    return list(self._dims)
