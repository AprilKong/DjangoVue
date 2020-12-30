<template>
  <el-table
    :data="tableData"
    stripe
    style="width: 100%">
    <el-table-column
      label="日期"
      min-width="180">
      <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px">{{ scope.row.date }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="寄存器"
      min-width="180">
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>姓名: {{ scope.row.name }}</p>
          <p>住址: {{ scope.row.address }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.name }}</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>
    <el-table-column
      prop="value"
      label="读数"
      min-width="180">
    </el-table-column>
    <el-table-column fixed="right" label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">设定阈值</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">移除报警</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
import {GetDeviceList} from '@/api/device'
  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-02',
          name: 'D700',
          value: 123,
          address: '蒸汽AD'
        }, {
          date: '2016-05-04',
          name: 'D701',
          value: 123,
          address: '气源AD'
        }, {
          date: '2016-05-01',
          name: 'D708',
          value: 123,
          address: '升温速率'
        }, {
          date: '2016-05-03',
          name: 'D800',
          value: 123,
          address: '炉内温度'
        }]
      }
    },
    async mounted() {
      var list = await GetDeviceList();
      console.log(list);
    },
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      }
    }
  }
</script>
